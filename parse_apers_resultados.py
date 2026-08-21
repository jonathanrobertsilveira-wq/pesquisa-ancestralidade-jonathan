from bs4 import BeautifulSoup
from pathlib import Path

html_path = Path('/home/ubuntu/upload/buscadocumentos.apers.rs.gov.br_lista-documentos_semHeaders_true_1787261954545.html')
text = html_path.read_text(encoding='utf-8', errors='ignore')
soup = BeautifulSoup(text, 'html.parser')
terms = ('MANOEL', 'GERALDO', 'LEMES', 'KENES', 'KENS', 'DORVALINA', 'DORALINA', 'TAPES', 'CAMAQUÃ', 'CAPELA')
print('RESULTADO_APERS')
print(soup.get_text(' ', strip=True)[:250])
for table in soup.find_all('table'):
    heading = table.find_previous(['div','h1','h2','h3','h4'])
    heading_text = heading.get_text(' ', strip=True) if heading else ''
    headers = [cell.get_text(' ', strip=True) for cell in table.find_all('th')]
    for row in table.find_all('tr'):
        cells = [cell.get_text(' ', strip=True) for cell in row.find_all('td')]
        if not cells:
            continue
        joined = ' | '.join(cells)
        upper = joined.upper()
        if any(term in upper for term in terms):
            print(f'GRUPO: {heading_text}')
            print(f'COLUNAS: {headers}')
            print(f'LINHA: {joined}')
