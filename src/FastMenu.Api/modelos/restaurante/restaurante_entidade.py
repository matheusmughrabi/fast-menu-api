from sqlalchemy import Column, String, Integer, DateTime, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  modelos.base.base_entidade import BaseEntidade

class RestauranteEntidade(BaseEntidade):
    __tablename__ = 'Restaurantes'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), unique=True)
    descricao = Column(UnicodeText, unique=False)
    id_conta = Column(Integer, ForeignKey('Contas.id'), nullable=False)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, descricao:str, id_conta: int):        
        self.nome = nome
        self.descricao = descricao
        self.id_conta = id_conta
