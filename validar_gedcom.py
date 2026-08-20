from pathlib import Path
import re

path = Path('/home/ubuntu/gedcom_pesquisa_jonathan/arvore_pesquisa_jonathan.ged')
lines = path.read_text(encoding='utf-8').splitlines()
errors = []
records = []
current = None
for n, line in enumerate(lines, 1):
    if not line.strip():
        errors.append(f'{n}: linha vazia')
        continue
    m = re.match(r'^(\d+)\s+(.*)$', line)
    if not m:
        errors.append(f'{n}: sintaxe de nível inválida: {line}')
        continue
    level = int(m.group(1))
    if level == 0:
        current = line
        records.append((n, line))
    elif level > 0 and current is None:
        errors.append(f'{n}: registro de nível {level} sem cabeçalho 0')

ids = set(re.findall(r'^0\s+(@[^@]+@)\s+', '\n'.join(lines), flags=re.M))
refs = set(re.findall(r'@[A-Z0-9_]+@', '\n'.join(lines)))
unknown_refs = sorted(refs - ids)
print(f'linhas={len(lines)} registros_nivel_0={len(records)} individuos={sum(1 for _,x in records if x.endswith(" INDI"))} familias={sum(1 for _,x in records if x.endswith(" FAM"))} fontes={sum(1 for _,x in records if x.endswith(" SOUR"))}')
print(f'referencias_desconhecidas={unknown_refs}')
print(f'linhas_com_erro={len(errors)}')
for err in errors[:20]:
    print('ERRO', err)
if unknown_refs or errors:
    raise SystemExit(1)
