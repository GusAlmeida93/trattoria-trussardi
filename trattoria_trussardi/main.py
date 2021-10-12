from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from trattoria_trussardi.schemas import schemas
from trattoria_trussardi.app import usuarios
from trattoria_trussardi.database import database

database.create_db()
app = FastAPI()

@app.get('/usuarios', status_code=status.HTTP_200_OK)
def listar_usuarios(db : Session = Depends(database.get_db)):
    lista_usuarios = usuarios.Usuarios(db).listar()
    return lista_usuarios

@app.post('/usuarios', status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario : schemas.Usuarios, db : Session = Depends(database.get_db)):
    usuario_criado = usuarios.Usuarios(db).criar(usuario)
    return usuario_criado