from sqlalchemy.orm import Session
from sqlalchemy import select
from trattoria_trussardi.schemas import schemas
from trattoria_trussardi.models import models

class Pedidos():
    
    def __init__(self, session : Session):
        self.session = session
    
    def criar(self, pedido : schemas.Pedidos):
        db_pedido = models.Pedidos(cliente_id = pedido.cliente_id,
                                     prato_id = pedido.prato_id,
                                     status = pedido.status)
        self.session.add(db_pedido)
        self.session.commit()
        self.session.refresh(db_pedido)
        return db_pedido

    def listar(self):
        
        query = select(models.Pedidos)
        pedidos = self.session.execute(query).scalars().all()
        
        return pedidos
        
    