from pathlib import Path
import csv
from collections import Counter

root = Path(__file__).resolve().parents[1]
path = root / 'docs/29_matriz_execucao_pesquisas_alema_2026-08-22.csv'
out = root / 'docs/31_cobertura_matriz_2026-08-22.txt'
with path.open(encoding='utf-8', newline='') as f:
    rows = list(csv.DictReader(f, delimiter=';'))
counts = Counter(r['id_pessoa'] for r in rows)
known = {f'A{i:02d}' for i in range(1, 37)}
missing = sorted(known - set(counts))
lines = [f'total_linhas {len(rows)}', f'candidatos_com_linhas {len(counts)}']
for code, count in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
    names = sorted({r['nome'] for r in rows if r['id_pessoa'] == code})
    lines.append(f'{code} {count} {names[0]}')
lines.append(f"candidatos_sem_linha {','.join(missing) if missing else 'nenhum'}")
out.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('\n'.join(lines))
