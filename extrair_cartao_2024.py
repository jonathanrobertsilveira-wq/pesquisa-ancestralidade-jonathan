from bs4 import BeautifulSoup
from pathlib import Path

html_path = Path('/home/ubuntu/upload/www.familysearch.org_en_tree_person_sources_9N2V-HKT_1787270282787.html')
html = html_path.read_text(errors='ignore')
soup = BeautifulSoup(html, 'html.parser')
needle = 'January 28, 2024'
for node in soup.find_all(string=lambda s: s and needle in s):
    print('TEXT:', repr(node.strip()))
    parent = node.parent
    for level in range(6):
        if parent is None:
            break
        print('LEVEL', level, 'TAG', parent.name, 'ATTRS', dict(parent.attrs))
        txt = ' '.join(parent.get_text(' ', strip=True).split())
        print('TEXTLEN', len(txt), 'TEXT', txt[:500])
        for a in parent.find_all('a', href=True):
            print('LINK', a.get('href'), 'TEXT', a.get_text(' ', strip=True)[:200])
        if level == 3:
            print('OUTERHTML', str(parent)[:12000])
        parent = parent.parent
    print('---')
