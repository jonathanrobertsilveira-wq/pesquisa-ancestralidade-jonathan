#!/usr/bin/env python3
from pathlib import Path
import requests

ark_id = "3:1:3Q9M-CS2Q-4Q7H-2"
base = f"https://sg30p0.familysearch.org/service/records/storage/deepzoomcloud/dz/v1/{ark_id}/image_files/10"
out = Path("/home/ubuntu/pesquisa-ancestralidade-jonathan/sources/karl_johann_img628_tiles_l10")
out.mkdir(parents=True, exist_ok=True)
for y in range(3):
    for x in range(4):
        path = out / f"{x}_{y}.jpg"
        url = f"{base}/{x}_{y}.jpg"
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        path.write_bytes(response.content)
        print(path, len(response.content))
