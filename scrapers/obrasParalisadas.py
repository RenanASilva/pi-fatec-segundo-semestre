import requests
from bs4 import BeautifulSoup
import re

pagina = requests.get('https://www.caraguatatuba.sp.gov.br/pmc/2022/03/obras-publicas/')
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')
divLinks = dados_pagina.find("div", class_="card-text position-relative")

# Obras paralisadas. (3 arquivos)
obrasParalisadas = divLinks.find_all(
    name="a",
    string=re.compile("Obras Paralisadas "),
    href=re.compile(r"Obras-Paralisadas.*?\.xlsx?$", re.IGNORECASE)
)

if obrasParalisadas:
    print(f"\n--- {len(obrasParalisadas)} ARQUIVOS OBRAS PARALISADAS ENCONTRADOS ---")
    for obra in obrasParalisadas:
        print(f"Texto: {obra.get_text(strip=True)}")
        print(f"URL: {obra.get('href')}\n")
else:
    print("Nenhum link correspondente encontrado para OBRAS PARALISADAS.")