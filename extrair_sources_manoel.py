from pathlib import Path
import re
from bs4 import BeautifulSoup

paths = sorted(Path('/home/ubuntu/upload').glob('www.familysearch.org_en_tree_person_sources_9N2V-HKT_*.html'))
if not paths:
    raise SystemExit('HTML do perfil não encontrado')
path = paths[-1]
html = path.read_text(errors='ignore')
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text(' ', strip=True)
urls = sorted(set(re.findall(r'https?://(?:www\.)?familysearch\.org/ark:/61903/1:1:[A-Z0-9-]+', html)))
print('ARks encontrados:')
for url in urls:
    print(url)
print('\nTítulos com datas reconhecíveis:')
for node in soup.find_all(string=re.compile(r'Manoel|Ozorio|Osorio|Tavares|Tavaros|Aparicio', re.I)):
    value = ' '.join(node.strip().split())
    if value and len(value) < 220:
        print(value)
