from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()



class Inscricao(BaseModel):
    id: Optional[int] = None
    nome: str


banco: List[Inscricao] = []


@app.get('/')
def home():
    return {'msg': 'API Funcionando'}

@app.post('/inscricao')
async def criar_cadastro(inscricao: Inscricao):
    inscricao.id = str(uuid4())

    banco.append(inscricao)
    return "Inscrição realizada com sucesso"

@app.get('/inscricao')
def listar_inscricao():
    return banco

@app.delete('/inscricao/{inscricao_id}')
def remover_animal(inscricao_id: str):
    for inscricao in banco:
        if inscricao.id == inscricao_id:
            nome = inscricao.nome
            banco.remove(inscricao)
            return {'msg': f'{nome} foi removido'}
    return {'erro': 'Animal não localizado'}