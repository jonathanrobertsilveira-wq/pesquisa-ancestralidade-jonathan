from pathlib import Path
from bs4 import BeautifulSoup

html = Path('/home/ubuntu/upload/www.familysearch.org_en_search_full-text_results_count_20_q.fullName_Regina_Schell_q.groupName_00463_1787413236909.html').read_text(encoding='utf-8', errors='replace')
soup = BeautifulSoup(html, 'html.parser')
for a in soup.find_all('a', href=True):
    text = ' '.join(a.get_text(' ', strip=True).split())
    if any(token in text for token in ('Baptism Records', 'Death Records', 'Santa Cristina')):
        print(text[:180], '\t', a['href'])
