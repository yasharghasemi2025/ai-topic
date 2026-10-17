from pathlib import Path
import json, shutil
import numpy as np
from PIL import Image

root=Path(__file__).parent
src=root/'frames'
dst=root/'normalized-frames'
dst.mkdir(exist_ok=True)
manifest=json.loads((src/'frames-manifest.json').read_text())
target_spacing=34.544344042838006
target_center=105.38060575635877
records=[]
for row in manifest['rows']:
    state=row['state']
    im=Image.open(src/state/'00.png').convert('RGBA')
    a=np.array(im).astype(int)
    yy,xx=np.where(a[:,:,3]>127)
    top,bottom=int(yy.min()),int(yy.max())
    mask=(a[:,:,1]>a[:,:,0]+30)&(a[:,:,1]>a[:,:,2]+30)&(a[:,:,3]>127)
    mask[np.indices(mask.shape)[0]>top+(bottom-top)*.45]=False
    y,x=np.where(mask)
    mid=(x.min()+x.max())/2
    centers=[(float(x[x<mid].mean()),float(y[x<mid].mean())),(float(x[x>mid].mean()),float(y[x>mid].mean()))]
    spacing=centers[1][0]-centers[0][0]
    if state in ['jumping','running-right','running-left']:
        scale,tx,ty=1.,0.,0.
        reason='Preserve airborne trajectory' if state=='jumping' else 'Profile eye projection is not frontal spacing; preserve matching locomotion pair and gait displacement. Visible single-eye height approximately 18 px, versus jumping 16 px.'
    else:
        scale=target_spacing/spacing
        tx=target_center-scale*(centers[0][0]+centers[1][0])/2
        ty=200-scale*bottom
        reason='One row-wide similarity transform matching frontal iris spacing and frame-0 baseline; other frames retain relative pose displacement.'
    outdir=dst/state
    outdir.mkdir(exist_ok=True)
    paths=[]
    for p in sorted((src/state).glob('*.png')):
        out=outdir/p.name
        if scale==1 and tx==0 and ty==0:
            shutil.copy2(p,out)
        else:
            img=Image.open(p).convert('RGBA')
            img=img.transform((192,208),Image.Transform.AFFINE,(1/scale,0,-tx/scale,0,1/scale,-ty/scale),Image.Resampling.BICUBIC)
            img.save(out)
        paths.append(str(out))
    row['frames']=paths
    records.append(dict(state=state,source_frame0_eye_centers=centers,source_eye_spacing=spacing,source_bottom=bottom,scale=scale,translation=[tx,ty],reason=reason))
(dst/'frames-manifest.json').write_text(json.dumps(manifest,indent=2))
(root/'qa'/'normalization-transforms.json').write_text(json.dumps(dict(target_eye_spacing=target_spacing,target_face_center=target_center,target_baseline=200,per_row=records),indent=2))
print(json.dumps(records,indent=2))
