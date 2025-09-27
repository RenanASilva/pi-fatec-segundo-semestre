import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

pagina = requests.get('https://www.caraguatatuba.sp.gov.br/pmc/2022/03/obras-publicas/')
dadosPagina = BeautifulSoup(pagina.text, 'html.parser')
divLinks = dadosPagina.find("div", class_="card-text position-relative")

# Obras em andamento. (41 arquivos)
obrasAndamento = divLinks.find_all(
    name="a",
    # attrs={"data-type": "URL"}, alguns nao tem esse data-type, tipo junho, julho, agosto, setembro de 2023
    string=re.compile("Relação de Obras em Execução"),
    href=re.compile(r"Andamento.*?\.xlsx?$", re.IGNORECASE)
)

if obrasAndamento:
    print(f"\n--- {len(obrasAndamento)} ARQUIVOS OBRAS EM ANDAMENTO ENCONTRADOS ---")
    for obra in obrasAndamento:
        print(f"Texto: {obra.get_text(strip=True)}")
        print(f"URL: {obra.get('href')}\n")
else:
    print("Nenhum link correspondente encontrado para OBRAS EM ANDAMENTO.")

# PANDAS:
urlTabela = obrasAndamento[0].get('href')
print("URL TABELA")
print(urlTabela)

infoTabela = pd.read_excel(urlTabela, header=2)
print(infoTabela.columns)
print(infoTabela['OBJETO'])