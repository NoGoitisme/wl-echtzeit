import os
from pathlib import Path
from urllib.parse import urlparse
import urllib.request

def getcsvdata(urls: list) -> None:
    Path("../data/csv/").mkdir(parents=True, exist_ok=True)
    for url in urls:
        try:
            p = Path("../data/csv/") / os.path.basename(urlparse(url).path)
            urllib.request.urlretrieve(url, p)
            print(p)
        except Exception as e:
            print(f"Error occurred while retrieving {url}: {e}")