from bs4 import BeautifulSoup
from pathlib import Path

html_path = Path('/home/ubuntu/upload/buscadocumentos.apers.rs.gov.br_lista-documentos_semHeaders_true_1787262441080.html')
soup = BeautifulSoup(html_path.read_text(encoding='utf-8', errors='ignore'), 'html.parser')
for table in soup.find_all('table'):
    headers = [cell.get_text(' ', strip=True) for cell in table.find_all('th')]
    for row in table.find_all('tr'):
        cells = [cell.get_text(' ', strip=True) for cell in row.find_all('td')]
        if not cells:
            continue
        joined = ' | '.join(cells)
        upper = joined.upper()
        if any(term in upper for term in ('DORVALINA', 'DORALINA', 'DORVALINO', 'DORALINO', 'KENES', 'KENS', 'CAMAQUÃ', 'CAMAQUA', 'TAPES', 'GRAVATAÍ')):
            print(f'LINHA: {joined}')
