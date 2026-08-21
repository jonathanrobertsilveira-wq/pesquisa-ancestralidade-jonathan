from pathlib import Path
from bs4 import BeautifulSoup

path = Path('/home/ubuntu/upload/www.familysearch.org_en_search_record_results_count_20_q.givenName_Gertrudes_20Ignacia_q.surname_Mar_1787274427559.html')
soup = BeautifulSoup(path.read_text(errors='ignore'), 'html.parser')
targets = {'Gertrudes Ignacia Martins', 'Gertrudes Inácia Martins', 'Gertrudes Inacia Martins', 'Gertrudes Ignacia Isenccia Martins', 'Gertrudes Ignacia Ignacia Martins', 'Geltrudes Ignacia Martins'}
seen = set()
for a in soup.find_all('a', href=True):
    text = ' '.join(a.get_text(' ', strip=True).split())
    href = a.get('href', '')
    if text not in targets or 'ark:/61903/1:1:' not in href:
        continue
    key = (text, href)
    if key in seen:
        continue
    seen.add(key)
    print('TARGET', text)
    print('HREF', href)
    node = a
    for level in range(1, 8):
        node = node.parent
        if node is None:
            break
        context = ' '.join(node.get_text(' ', strip=True).split())
        if len(context) > 180:
            print('CONTEXT_LEVEL', level, context[:2200])
            break
    print()
