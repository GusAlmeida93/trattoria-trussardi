from sqlalchemy.orm import Session
from trattoria_trussardi.schemas import schemas
from trattoria_trussardi.models import models

class Usuarios():
    
    def __init__(self, db : Session = None):
        self.session = db
    
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
        
        usuarios = self.session.query(models.Usuarios).all()
        
        return usuarios
        
    