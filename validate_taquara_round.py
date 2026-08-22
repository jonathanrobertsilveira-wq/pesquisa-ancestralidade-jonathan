import csv
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent
errors = []

csv_path = ROOT / 'docs/36_matriz_evidencias_registros_taquara_2026-08-22.csv'
with csv_path.open(encoding='utf-8', newline='') as f:
    rows = list(csv.DictReader(f))
if len(rows) != 31:
    errors.append(f'CSV deveria ter 31 linhas de evidência; tem {len(rows)}')
expected = {'id','proposição','fonte','trecho ou campo','status','confiança','limitação','próximo passo'}
if set(rows[0]) != expected:
    errors.append(f'colunas inesperadas: {set(rows[0])}')
ids = [int(r['id']) for r in rows]
if ids != list(range(1, 32)):
    errors.append(f'IDs não sequenciais: {ids}')

for rel in [
    'docs/35_transcricao_analise_registros_manuscritos_taquara_2026-08-22.md',
    'docs/36_matriz_evidencias_registros_taquara_2026-08-22.csv',
    'docs/37_diario_investigacao_taquara_2026-08-22.md',
    'docs/38_pedido_referencia_e_paginas_taquara_2026-08-22.md',
    'docs/39_avaliacao_ponte_schell_taquara_2026-08-22.md',
    'docs/40_status_rodada_taquara_2026-08-22.md',
    'sources/recebidos_2026-08-22/imagens_manuscritas/registro_casamentos_taquara.webp',
    'sources/recebidos_2026-08-22/imagens_manuscritas/registros_obitos_taquara.webp',
    'sources/recebidos_2026-08-22/imagens_manuscritas/SHA256SUMS.txt',
]:
    if not (ROOT / rel).exists():
        errors.append(f'arquivo ausente: {rel}')

# Validate local markdown links only.
for md in [ROOT/'README.md', ROOT/'docs/00_indice_projeto_2026-08-20.md', *sorted((ROOT/'docs').glob('35_*.md')), *sorted((ROOT/'docs').glob('37_*.md')), *sorted((ROOT/'docs').glob('38_*.md')), *sorted((ROOT/'docs').glob('39_*.md')), *sorted((ROOT/'docs').glob('40_*.md'))]:
    text = md.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
        if target.startswith(('http://','https://','mailto:','#')):
            continue
        target_path = (md.parent / target.split('#',1)[0]).resolve()
        if not target_path.exists():
            errors.append(f'link quebrado em {md.relative_to(ROOT)}: {target}')

res = subprocess.run(['sha256sum','-c','sources/recebidos_2026-08-22/imagens_manuscritas/SHA256SUMS.txt'], cwd=ROOT, text=True, capture_output=True)
if res.returncode != 0:
    errors.append('falha na verificação SHA-256')

if errors:
    print('VALIDAÇÃO FALHOU')
    for e in errors:
        print('-', e)
    raise SystemExit(1)
print('VALIDAÇÃO OK')
print('evidencias_csv=', len(rows))
print('links_locais=OK')
print('hashes=OK')
