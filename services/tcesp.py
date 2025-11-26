import requests

BASE_URL = "https://transparencia.tce.sp.gov.br/api"


def get_municipios():
    """Retorna lista de municípios da API do TCE."""
    url = f"{BASE_URL}/json/municipios"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.json()     # <-- retorna dados internos, não resposta HTTP


def get_despesas(municipio, ano, mes):
    """Retorna despesas filtradas da API do TCE."""
    url = f"{BASE_URL}/json/despesas/{municipio}/{ano}/{mes}"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.json()