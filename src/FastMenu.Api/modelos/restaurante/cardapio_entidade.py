from sqlalchemy import Column, String, Integer, DateTime, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  modelos.base.base_entidade import BaseEntidade

class CardapioEntidade(BaseEntidade):
    __tablename__ = 'Cardapios'

    id = Column(Integer, primary_key=True)
    id_restaurante = Column(Integer, ForeignKey('Restaurantes.id'), nullable=False)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, id_restaurante:int):        
        self.id_restaurante = id_restaurante