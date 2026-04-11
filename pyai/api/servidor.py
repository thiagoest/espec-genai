from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
import datetime

app = FastAPI()

dict_pessoas = {}

@app.get('/teste_async')
async def teste(id: int):
    return "Teste " + str(id)

@app.post("/adicionar-pessoa")
def adicionar_pessoa(cpf: int, nome: str):
    if cpf in dict_pessoas:
        raise HTTPException(status_code=400, detail="CPF já cadastrado.")
    dict_pessoas[cpf] = (cpf, nome)

@app.get('/nome-pessoa/{cpf}')
def nome_pessoa(cpf: int):
    if cpf not in dict_pessoas:
        raise HTTPException(status_code=400, detail="Pessoa inexistente.")
    return dict_pessoas[cpf][1]

@app.get('/saudacao')
def saudacao():
    return {'saudacao': 'Olá Mundo!'}

@app.get('/hora_atual')
def hora_atual():
    return {'hora': str(datetime.datetime.now())}

@app.get('/verificar-cpf/{cpf_teste}')
def verificar_cpf(cpf_teste: Annotated[int, Path(title="CPF", description="O CPF a ser testado", ge=1, le=99999999999)]):

    #cpf_teste = int(cpf_teste)

    somatorio_valida_ultimo = 0
    somatorio_valida_penultimo = 0
    ultimo = cpf_teste % 10
    cpf_teste //= 10
    penultimo = cpf_teste % 10
    cpf_teste //= 10
    somatorio_valida_ultimo = penultimo * 2
    for i in range(2, 12):
        modulo = cpf_teste % 10
        cpf_teste //= 10
        somatorio_valida_penultimo += modulo * i
        somatorio_valida_ultimo += modulo * (i + 1)
        modulo = somatorio_valida_penultimo % 11

    if modulo < 2:
        if penultimo != 0:
            return False # CPF inválido
    else:
        if penultimo != 11 - modulo:
            return False # CPF inválido
    modulo = somatorio_valida_ultimo % 11

    if modulo < 2:
        if ultimo != 0:
            return False # CPF inválido
    else:
        if penultimo != 11 - modulo:
            return False # CPF inválido
    modulo = somatorio_valida_ultimo % 11

    if modulo < 2:
        if ultimo != 0:
            return False # CPF inválido
    else:
        if ultimo != 11 - modulo:
            return False # CPF inválido
    return True # CPF válido    