from sqlalchemy.orm import Session
from trattoria_trussardi.schemas import schemas
from trattoria_trussardi.models import models

class Pratos():
    
    def __init__(self, session : Session):
        self.session = session
    
    def criar(self, prato : schemas.Pratos):
        db_prato = models.Pratos(nome = prato.nome,
                                     tipo = prato.tipo,
                                     disponivel = prato.disponivel,
                                     preco = prato.preco)
        self.session.add(db_prato)
        self.session.commit()
        self.session.refresh(db_prato)
        return db_prato

    def listar(self):
        
        pratos = self.session.query(models.Pratos).all()
        
        return pratos