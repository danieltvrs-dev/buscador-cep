# Buscador de CEP

![Python](https://img.shields.io/badge/Python-3.13-e8132a?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.135-e8132a?style=flat-square&logo=fastapi&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-22c55e?style=flat-square)

API que recebe um CEP e retorna o endereço completo consultando o ViaCEP, uma API pública e gratuita do governo brasileiro.

---

## Como funciona

Você manda um CEP, a API valida o formato, consulta o ViaCEP e devolve o endereço formatado. Se o CEP não existir ou for inválido, retorna um erro claro.

| Rota | O que faz |
|------|-----------|
| `/` | Verifica se a API está no ar |
| `/cep/{cep}` | Retorna o endereço do CEP informado |

Exemplos:

```
/cep/49890000        → Nossa Senhora de Lourdes, SE
/cep/01310100        → Avenida Paulista, São Paulo, SP
/cep/49890-000       → funciona com ou sem traço
/cep/00000000        → CEP não encontrado
/cep/abc             → CEP inválido
```

---

## Como rodar

```bash
git clone https://github.com/danieltvrs-dev/buscador-cep.git
cd buscador-cep
pip install fastapi uvicorn httpx
uvicorn main:app --reload
```

Acesse: `http://127.0.0.1:8000`
Documentação: `http://127.0.0.1:8000/docs`

---

## O que aprendi aqui

Aprendi a fazer minha API conversar com outra API — algo que não existia na calculadora. Aqui precisei usar o `httpx` pra buscar dados no ViaCEP, entender o que é `async/await` e por que ele existe, e tratar diferentes tipos de erro antes mesmo de fazer a requisição. Foi a primeira vez que meu código dependeu de algo externo pra funcionar.

---

**Daniel Tavares** — [LinkedIn](https://www.linkedin.com/in/daniel-campostvrs) · [GitHub](https://github.com/danieltvrs-dev)
