import requests
from bs4 import BeautifulSoup
import re

pagina = requests.get('https://www.caraguatatuba.sp.gov.br/pmc/2022/03/obras-publicas/')
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')
divLinks = dados_pagina.find("div", class_="card-text position-relative")

# Relatório anual de obras concluídas. (3 arquivos)
relatoriosObrasConcluidas = divLinks.find_all(
    name="a",
    string=re.compile("Relatório Anual de Obras Concluídas"),
    href=re.compile(r"Obras-Concluidas.*?\.pdf$", re.IGNORECASE)
)

if relatoriosObrasConcluidas:
    print(f"\n--- {len(relatoriosObrasConcluidas)} ARQUIVOS RELATÓRIOS ANUAIS ENCONTRADOS ---")
    for relatorio in relatoriosObrasConcluidas:
        print(f"Texto: {relatorio.get_text(strip=True)}")
        print(f"URL: {relatorio.get('href')}\n")
else:
    print("Nenhum link correspondente encontrado para RELATÓRIOS ANUAIS.")