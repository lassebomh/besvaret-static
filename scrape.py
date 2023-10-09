# %%

import xml.etree.ElementTree as ET
from pathlib import Path

import requests
from urllib3.util import parse_url

folder = Path("~/Desktop/besvaret-dl/").absolute()

# %%


# Parse XML
sitemap = ET.fromstring(requests.get("https://besvaret.dk/sitemap.xml").text)

# %%

# print(sitemap)

# Access elements and attributes
for page in sitemap:
    url = page[0].text
    path = parse_url(url).path

    Path("./docs" + path).absolute().mkdir(exist_ok=True)

    with open("./docs" + path + "index.html", "w") as f:
        f.write(requests.get(url).text)

    print(url)
