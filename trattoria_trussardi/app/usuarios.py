from sqlalchemy.orm import Session
from sqlalchemy import select
from trattoria_trussardi.schemas import schemas
from trattoria_trussardi.models import models

class Usuarios():
    
    def __init__(self, session : Session):
        self.session = session
    
    def criar(self, usuario : schemas.Usuarios):
        db_usuario = models.Usuarios(nome = usuario.nome,
                                     email = usuario.email,
                                     senha = usuario.senha,
                                     tipo_acesso = usuario.tipo_acesso)
        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)
        return db_usuario

    def listar(self):
        
        query = select(models.Usuarios)
        usuarios = self.session.execute(query).scalars().all()
        
        return usuarios
        
    