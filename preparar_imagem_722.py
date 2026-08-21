from PIL import Image, ImageEnhance, ImageFilter
from pathlib import Path

src = Path('/home/ubuntu/upload/3QS7-99GW-13V7.webp')
out = Path('/home/ubuntu/pesquisa-ancestralidade-jonathan/imagem_722_recortes')
out.mkdir(exist_ok=True)
img = Image.open(src).convert('L')
# Preserve the whole document with gentle contrast enhancement.
whole = ImageEnhance.Contrast(img).enhance(1.45)
whole = ImageEnhance.Sharpness(whole).enhance(1.6)
whole.save(out / 'documento_contraste.png')
# Crop left and right pages with overlap; the right page contains the continuation.
w, h = img.size
crops = {
    'pagina_esquerda': (80, 35, 1035, h-20),
    'pagina_direita': (950, 35, 1965, h-20),
    'direita_superior': (980, 40, 1965, 720),
    'direita_inferior': (980, 620, 1965, h-20),
    'esquerda_inferior': (80, 520, 1035, h-20),
}
for name, box in crops.items():
    c = img.crop(box)
    c = ImageEnhance.Contrast(c).enhance(1.55)
    c = ImageEnhance.Sharpness(c).enhance(1.8)
    c.save(out / f'{name}.png')
print(f'created {len(crops)+1} images in {out}')
print(f'original dimensions: {w}x{h}')
