from pathlib import Path
import csv
from collections import Counter

root = Path('/home/ubuntu/pesquisa-ancestralidade-jonathan')
path = root / 'docs/29_matriz_execucao_pesquisas_alema_2026-08-22.csv'
rows=[]
with path.open(encoding='utf-8', newline='') as f:
    for row in csv.DictReader(f, delimiter=';'):
        rows.append(row)
counts=Counter(r['id_pessoa'] for r in rows)
print('total_linhas', len(rows))
print('candidatos_com_linhas', len(counts))
for code,count in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
    names=sorted({r['nome'] for r in rows if r['id_pessoa']==code})
    print(code, count, names[0])
missing=[]
known={f'A{i:02d}' for i in range(1,37)}
for code in sorted(known):
    if code not in counts:
        missing.append(code)
print('candidatos_sem_linha', ','.join(missing) if missing else 'nenhum')
(root/'docs/31_cobertura_matriz_2026-08-22.txt').write_text('\n'.join([f'{code}\t{count}' for code,count in sorted(counts.items())])+'\n',encoding='utf-8')
