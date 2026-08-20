import csv
from pathlib import Path

terms = [
    "ROSALVINO", "VALDECI", "CAROLINA AUGUSTA", "FLAULIANO", "MANOEL GERALDO",
    "RAIMUNDO JOSE", "RAIMUNDO JOSÉ", "ALICIA SCHELL", "CERRO GRANDE", "TAPES",
    "KENES DE SOUZA", "KENNE"
]
for path in sorted(Path('.').rglob('*.csv')):
    print(f"=== {path} ===")
    with path.open(encoding='utf-8-sig', errors='replace', newline='') as fh:
        rows = csv.reader(fh)
        for idx, row in enumerate(rows):
            text = ' | '.join(row)
            upper = text.upper()
            if any(term in upper for term in terms):
                print(f"{idx}: {text[:900]}")
