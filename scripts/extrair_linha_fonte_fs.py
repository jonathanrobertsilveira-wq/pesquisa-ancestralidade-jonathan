from bs4 import BeautifulSoup
from pathlib import Path

html_path = Path('/home/ubuntu/upload/www.familysearch.org_en_tree_person_sources_KJ8D-X45_1787410842826.html')
html = html_path.read_text(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
for year in soup.find_all(string=lambda value: value and value.strip() == '1891'):
    row = year.parent
    for _ in range(8):
        if row is None:
            break
        print('NODE', row.name, 'class=', row.get('class'), 'role=', row.get('role'), 'data=', {k:v for k,v in row.attrs.items() if k not in {'class','style'}})
        print('TEXT', row.get_text(' ', strip=True)[:800])
        for link in row.find_all('a', href=True):
            print('LINK', link.get('href'), link.get_text(' ', strip=True)[:200])
        row = row.parent
    print('---')
