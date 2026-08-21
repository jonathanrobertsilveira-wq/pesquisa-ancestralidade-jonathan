from bs4 import BeautifulSoup
from pathlib import Path
import re

path = Path('/home/ubuntu/upload/www.familysearch.org_en_tree_person_sources_GV4D-FLS_1787262724727.html')
soup = BeautifulSoup(path.read_text(encoding='utf-8', errors='ignore'), 'html.parser')
seen = set()
for tag in soup.find_all(True):
    text = ' '.join(tag.get_text(' ', strip=True).split())
    if not text:
        continue
    hrefs = []
    for a in tag.find_all('a', href=True):
        hrefs.append(a['href'])
    ids = re.findall(r'(?:ark:/61903/1:1:|ark:/61903/3:1:)[A-Z0-9-]+', ' '.join(hrefs) + ' ' + text)
    if ids:
        key = (text[:240], tuple(ids))
        if key not in seen:
            seen.add(key)
            print('TEXT:', text[:240])
            print('IDS:', ', '.join(ids))
