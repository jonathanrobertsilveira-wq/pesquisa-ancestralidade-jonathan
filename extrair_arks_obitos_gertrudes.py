from pathlib import Path
from bs4 import BeautifulSoup

path = Path('/home/ubuntu/upload/www.familysearch.org_en_search_record_results_count_20_q.collectionId_3741255_q.givenName_Gertrudes__1787274135235.html')
soup = BeautifulSoup(path.read_text(errors='ignore'), 'html.parser')
targets = ['Gertrudes Inacia Martins', 'Gertrudes Inácia Martins']
seen = set()
for a in soup.find_all('a', href=True):
    text = ' '.join(a.get_text(' ', strip=True).split())
    if text not in targets or 'ark:/61903/1:1:' not in a.get('href', ''):
        continue
    key = (text, a['href'])
    if key in seen:
        continue
    seen.add(key)
    print('TARGET', text)
    print('HREF', a['href'])
    node = a
    for level in range(1, 8):
        node = node.parent
        if node is None:
            break
        context = ' '.join(node.get_text(' ', strip=True).split())
        if len(context) > 180:
            print('CONTEXT_LEVEL', level, context[:2000])
            break
    print()
