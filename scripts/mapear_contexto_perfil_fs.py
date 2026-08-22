from pathlib import Path
import re

path = Path('/home/ubuntu/upload/www.familysearch.org_en_tree_person_details_LBHB-QJH_1787413781382.html')
text = path.read_text(encoding='utf-8', errors='replace')
ids = sorted(set(re.findall(r'LB[A-Z0-9-]{4,}', text)))
for ident in ids:
    print(f'\n### {ident}')
    for match in list(re.finditer(re.escape(ident), text))[:3]:
        start = max(0, match.start() - 300)
        end = min(len(text), match.end() + 300)
        snippet = re.sub(r'\\s+', ' ', text[start:end])
        print(snippet[:650])
