from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from trattoria_trussardi.schemas import schemas
from trattoria_trussardi.app import clientes, usuarios, pedidos, pratos
from trattoria_trussardi.database import database

database.create_db()
app = FastAPI()

@app.get('/usuarios', status_code=status.HTTP_200_OK, response_model= List[schemas.UsuariosResponse])
def listar_usuarios(db : Session = Depends(database.get_db)):
    lista_usuarios = usuarios.Usuarios(db).listar()
    return lista_usuarios

@app.post('/usuarios', status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario : schemas.Usuarios, db : Session = Depends(database.get_db)):
    usuario_criado = usuarios.Usuarios(db).criar(usuario)
    return usuario_criado

@app.get('/clientes', status_code=status.HTTP_200_OK, response_model= List[schemas.ClientesResponse])
def listar_clientes(db : Session = Depends(database.get_db)):
    lista_clientes = clientes.Clientes(db).listar()
    return lista_clientes

@app.post('/clientes', status_code=status.HTTP_201_CREATED)
def criar_cliente(cliente : schemas.Clientes, db : Session = Depends(database.get_db)):
    cliente_criado = clientes.Clientes(db).criar(cliente)
    return cliente_criado

@app.get('/pedidos', status_code=status.HTTP_200_OK, response_model= List[schemas.Pedidos])
def listar_pedidos(db : Session = Depends(database.get_db)):
    lista_pedidos = pedidos.Pedidos(db).listar()
    return lista_pedidos

@app.post('/pedidos', status_code=status.HTTP_201_CREATED)
def criar_pedido(pedido : schemas.Pedidos, db : Session = Depends(database.get_db)):
    pedido_criado = pedidos.Pedidos(db).criar(pedido)
    return pedido_criado

@app.get('/pratos', status_code=status.HTTP_200_OK, response_model= List[schemas.Pratos])
def listar_pratos(db : Session = Depends(database.get_db)):
    lista_pratos = pratos.Pratos(db).listar()
    return lista_pratos

@app.post('/pratos', status_code=status.HTTP_201_CREATED)
def criar_prato(prato : schemas.Pratos, db : Session = Depends(database.get_db)):
    prato_criado = pratos.Pratos(db).criar(prato)
    return prato_criado

