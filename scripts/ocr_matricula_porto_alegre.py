from pathlib import Path
import subprocess
import re

base = Path('/home/ubuntu/pesquisa-ancestralidade-jonathan/sources')
pdf = base / 'konsulatsmatrikel-porto-alegre-s-z-data.pdf'
imgdir = base / 'matricula_s_z_pages'
imgdir.mkdir(exist_ok=True)

subprocess.run([
    'pdftoppm', '-png', '-r', '170', str(pdf), str(imgdir / 'page')
], check=True)

hits = []
for image in sorted(imgdir.glob('page-*.png')):
    outbase = image.with_suffix('')
    txt = outbase.with_suffix('.txt')
    subprocess.run([
        'tesseract', str(image), str(outbase), '-l', 'deu+eng', '--psm', '6'
    ], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    content = txt.read_text(errors='replace') if txt.exists() else ''
    if re.search(r'schell|schnell|nicolaus|nikolaus|nicolau|johann|karl|carlos', content, re.I):
        hits.append((image.name, content))

report = base / 'matricula_s_z_ocr_hits.txt'
with report.open('w', encoding='utf-8') as f:
    f.write('OCR da matrícula consular Porto Alegre S-Z\n')
    f.write('Consulta: Schell|Schnell|Nicolaus|Nikolaus|Nicolau|Johann|Karl|Carlos\n\n')
    if not hits:
        f.write('Nenhuma ocorrência textual detectada pelo OCR.\n')
    for name, content in hits:
        f.write(f'===== {name} =====\n{content}\n')

print(f'Páginas renderizadas: {len(list(imgdir.glob("page-*.png")))}')
print(f'Páginas com ocorrência OCR: {len(hits)}')
print(f'Relatório: {report}')
