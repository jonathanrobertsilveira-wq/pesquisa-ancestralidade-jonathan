from bs4 import BeautifulSoup
from pathlib import Path
import re

path = Path('/home/ubuntu/upload/www.familysearch.org_en_search_film_004634195_i_0_1787411258893.html')
html = path.read_text(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
print('bytes', len(html))
for pat in ['waypoint', 'alternative', 'booklet', 'imageNumber', 'filmNumber', 'groupName', 'DGS']:
    print('PATTERN', pat, html.lower().count(pat.lower()))
for tag in soup.find_all(['a','button','option','li','div']):
    text = ' '.join(tag.get_text(' ', strip=True).split())
    attrs = ' '.join(f'{k}={v}' for k,v in tag.attrs.items() if k in {'href','id','aria-label','role','data-testid','data-manus-click-id'})
    if text and any(word in text.lower() for word in ['film #', 'waypoint', 'rio pardo', 'batism', 'bapt', 'registros']):
        print('ELEMENT', tag.name, attrs, repr(text[:500]))
print('URLS')
for href in sorted(set(re.findall(r'https?[^" ]+|/en/search/film/[^" ]+', html))):
    if 'film' in href.lower() or '939N' in href:
        print(href[:500])
