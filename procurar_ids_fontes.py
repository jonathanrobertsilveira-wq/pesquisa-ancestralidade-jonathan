import re
from pathlib import Path

html = Path('/home/ubuntu/upload/www.familysearch.org_en_tree_person_sources_9N2V-HKT_1787270282787.html').read_text(errors='ignore')
needles = ['January 28, 2023', 'January 28, 2024', 'Manoel Osorio Tavares', 'sourceId', 'XSXL-RN52']
for needle in needles:
    print('\n###', needle)
    positions = [m.start() for m in re.finditer(re.escape(needle), html)]
    print('COUNT', len(positions))
    for pos in positions[:8]:
        print('---POS', pos)
        print(html[max(0,pos-1200):pos+1800])
