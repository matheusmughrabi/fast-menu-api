from sqlalchemy import Column, String, Integer, DateTime, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  modelos.base.base_entidade import BaseEntidade

class CardapioSecaoEntidade(BaseEntidade):
    __tablename__ = 'CardapioSecao'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), unique=True)
    id_cardapio = Column(Integer, ForeignKey('Cardapios.id'), nullable=False)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, id_cardapio:int):        
        self.nome = nome
        self.id_cardapio = id_cardapio
