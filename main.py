import httpx
from fastapi import FastAPI

app = FastAPI(
    title="Buscador de CEP",
    description="API para consulta de endereços a partir do CEP.",
    version="1.0.0"
)

@app.get("/")
def inicio():
    return {"mensagem": "Buscador de CEP funcionando!"} 

@app.get("/cep/{cep}")
async def buscar_cep(cep: str):

    cep = cep.replace("-", "").replace(" ", "")
   
    if len(cep) != 8 or not cep.isdigit():
        return {"erro": "CEP inválido. Digite apenas os 8 números."}

    async with httpx.AsyncClient() as client:
        resposta = await client.get(f"https://viacep.com.br/ws/{cep}/json/")

    dados = resposta.json()

    if "erro" in dados:
        return {"erro": "CEP não encontrado."}

    return {
        "cep": dados.get("cep"),
        "logradouro": dados.get("logradouro"),
        "bairro": dados.get("bairro"),
        "cidade": dados.get("localidade"),
        "estado": dados.get("uf"),
        "ibge": dados.get("ibge")
    }
