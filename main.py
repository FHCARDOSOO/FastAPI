from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class Clientes(BaseModel):
    id: Optional[int] = 0
    nome: str
    sobrenome: str
    email: str
    senha: str

db_clientes =[
    Clientes(id=1, nome= 'Fernando', sobrenome= 'Cardoso', email = 'fernando@email.com', senha = '123'),
    Clientes(id=2, nome= 'Arthur', sobrenome= 'Cardoso', email = 'arthur@email.com', senha = '123'),
    Clientes(id=3, nome= 'Maria', sobrenome= 'Cardoso', email = 'maria@email.com', senha = '123'),
    Clientes(id=4, nome= 'KArina', sobrenome= 'Cardoso', email = 'karina@email.com', senha = '123'),
    
]


@app.get('/')
def home():
    return {'mensagem':'Minha API está no AR'}

@app.get('/clientes/')
async def todos_usuarios():
    return {'clientes': db_clientes}


@app.get("/clientes/{id}")
async def mostrar_usuarios(email: str):
    return{'clientes': [cliente for cliente in db_clientes if cliente.email == email]}

@app.post("/cadastrar_clientes/")
async def cadastrar_cliente(clientes: Clientes):
    clientes.id = db_clientes[-1].id + 1
    db_clientes.append(clientes)
    return{'mensagem':'Cliente Inserido com Sucesso'}

@app.patch("/atualizar_clientes/{id}")
async def atualiza_cliente(id: int,clientes: Clientes):
    index = [index for index, clientes in enumerate(db_clientes) if clientes.id == id]
    clientes.id = db_clientes[index[0]].id
    db_clientes[index[0]] = clientes
    return {'mensagem':'Cliente Atualizado com Sucesso'}

@app.delete("/produtos/{id}")
async def deletar_cliente(email: str):
    cliente= [ cliente for cliente in db_clientes if cliente.email == email]
    db_clientes.remove(cliente[0])
    return{'mensagem':'Cliente Removido com Sucesso'}