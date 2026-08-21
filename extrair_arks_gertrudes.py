from pathlib import Path
from bs4 import BeautifulSoup
import re

paths = sorted(Path('/home/ubuntu/upload').glob('www.familysearch.org_en_search_record_results*.html'), key=lambda p: p.stat().st_mtime, reverse=True)
for path in paths:
    html = path.read_text(errors='ignore')
    soup = BeautifulSoup(html, 'html.parser')
    print(f'FILE: {path}')
    seen = set()
    for a in soup.find_all('a', href=True):
        href = a.get('href', '')
        if 'ark:/61903/1:1:' not in href:
            continue
        text = ' '.join(a.get_text(' ', strip=True).split())
        parent = a.parent.get_text(' ', strip=True) if a.parent else ''
        context = ' '.join(parent.split())
        key = (href, text, context[:500])
        if key in seen:
            continue
        seen.add(key)
        if any(term.lower() in (text + ' ' + context).lower() for term in ['cavares', 'candida', 'manoe', 'manoel', 'martins', 'tavares', 'gertrudes']):
            print('HREF:', href)
            print('TEXT:', text)
            print('CONTEXT:', context[:800])
    print()
