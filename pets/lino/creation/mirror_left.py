from pathlib import Path
from PIL import Image, ImageOps
import json

root = Path(__file__).parent
source = root / 'qa/rows/running-right/frames/running-right'
target = root / 'decoded/running-left.png'
strip = Image.new('RGBA', (1536,208))
for i, path in enumerate(sorted(source.glob('*.png'))):
    with Image.open(path) as frame:
        strip.alpha_composite(ImageOps.mirror(frame.convert('RGBA')), (192*i,0))
strip.save(target)
manifest_path = root / 'imagegen-jobs.json'
manifest = json.loads(manifest_path.read_text())
for job in manifest['jobs']:
    if job['id'] in ['base','idle','waving','running-right']:
        job['status']='complete'
    if job['id']=='running-left':
        job['derived_from']='running-right'
        job['mirror_decision']={'approved':True,'note':'Symmetric tuxedo markings, flat lighting and no handed props; mirror each extracted complete frame, preserving temporal order.'}
manifest_path.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
