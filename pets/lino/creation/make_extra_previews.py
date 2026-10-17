"""Render preview-only files from the exact encoded final atlas."""
from pathlib import Path
import sys
import subprocess
from PIL import Image, ImageDraw

root = Path(__file__).parent
atlas = Image.open(root / 'final/spritesheet-extended.png').convert('RGBA')
out = root / 'final/previews'
out.mkdir(parents=True, exist_ok=True)
specs = [('idle',6),('running-right',8),('running-left',8),('waving',4),('jumping',5),('failed',8),('waiting',6),('running',6),('review',6),('look-a',8),('look-b',8)]
frames=[]
for r,(name,count) in enumerate(specs):
    for c in range(count):
        cell = atlas.crop((192*c,208*r,192*(c+1),208*(r+1)))
        if r < 9:
            frame_dir = root / 'final/frames' / name
            frame_dir.mkdir(parents=True,exist_ok=True)
            cell.save(frame_dir / f'{c:02d}.png')
        stage = Image.new('RGB',(384,256),'#edf2f6')
        stage.paste(cell,(96,28),cell)
        ImageDraw.Draw(stage).text((12,8),f'{name} {c+1}/{count}',fill='#203040')
        frames.append(stage)
frames[0].save(out/'all-states.gif',save_all=True,append_images=frames[1:],duration=170,loop=0)
look=frames[-16:]
look[0].save(out/'look-loop.gif',save_all=True,append_images=look[1:],duration=200,loop=0)
jump=frames[:6]+frames[26:31]+frames[:6]
jump[0].save(out/'idle-jump-idle.gif',save_all=True,append_images=jump[1:],duration=170,loop=0)
stills=Image.new('RGB',(384*4,256),'#edf2f6')
for i,index in enumerate([0,24,28,30]):
    stills.paste(frames[index],(384*i,0))
stills.save(out/'motion-stills.png')
sys.path.insert(0,str(root.parent/'python-packages'))
import imageio_ffmpeg
command=[imageio_ffmpeg.get_ffmpeg_exe(),'-y','-i',str(out/'all-states.gif'),'-vf','format=yuv420p','-movflags','+faststart',str(out/'all-states.mp4')]
subprocess.run(command,check=True,capture_output=True)
print(out)
