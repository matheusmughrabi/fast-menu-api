from sqlalchemy import Column, String, Integer, DateTime, UnicodeText, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  modelos.base.base_entidade import BaseEntidade

class CardapioItemEntidade(BaseEntidade):
    __tablename__ = 'CardapioItem'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False, unique=False)
    valor = Column(Float, nullable=False, unique=False)
    id_cardapio_secao = Column(Integer, ForeignKey('CardapioSecao.id'), nullable=False)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, valor:float, id_cardapio_secao: int):        
        self.nome = nome
        self.valor = valor
        self.id_cardapio_secao = id_cardapio_secao
