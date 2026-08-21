from pathlib import Path
from io import BytesIO
import requests
from PIL import Image

base = 'https://sg30p0.familysearch.org/service/records/storage/deepzoomcloud/dz/v1/apid:TH-1-14861-63927-37/image_files/10'
out = Path('/home/ubuntu/pesquisa-ancestralidade-jonathan/imagem_779_tiles')
out.mkdir(parents=True, exist_ok=True)
for y in range(4):
    for x in range(4):
        path = out / f'{x}_{y}.jpg'
        if not path.exists():
            r = requests.get(f'{base}/{x}_{y}.jpg', timeout=60)
            r.raise_for_status()
            path.write_bytes(r.content)
        print(path.name, path.stat().st_size)

imgs = {}
for y in range(4):
    for x in range(4):
        imgs[(x, y)] = Image.open(out / f'{x}_{y}.jpg').convert('RGB')
tw = max(im.width for im in imgs.values())
th = max(im.height for im in imgs.values())
canvas = Image.new('RGB', (tw * 4, th * 4), 'black')
for (x, y), im in imgs.items():
    canvas.paste(im, (x * tw, y * th))
output = Path('/home/ubuntu/pesquisa-ancestralidade-jonathan/imagem_779_montada.jpg')
canvas.save(output, quality=95)
print(f'OUTPUT {output} {canvas.size}')
