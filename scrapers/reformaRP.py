import requests
from bs4 import BeautifulSoup
import re

pagina = requests.get('https://www.caraguatatuba.sp.gov.br/pmc/2022/03/obras-publicas/')
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')
divLinks = dados_pagina.find("div", class_="card-text position-relative")

# Obras em Andamento – Reforma das Redes Pluviais. (1 arquivo) 
reformaRedesPluviais = divLinks.find_all(
    name="a",
    string=re.compile("Reforma das RPs"),
    href=re.compile(r"Reforma-RP.*?\.xlsx?$", re.IGNORECASE)
)

if reformaRedesPluviais:
    print(f"\n--- {len(reformaRedesPluviais)} ARQUIVOS REFORMA DAS REDES PLUVIAIS ENCONTRADOS ---")
    for reforma in reformaRedesPluviais:
        print(f"Texto: {reforma.get_text(strip=True)}")
        print(f"URL: {reforma.get('href')}\n")
else:
    print("Nenhum link correspondente encontrado para REFORMA DAS REDES PLUVIAIS.")