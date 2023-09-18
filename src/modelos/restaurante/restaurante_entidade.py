from sqlalchemy import Column, String, Integer, DateTime, UnicodeText
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  modelos.base.base_entidade import BaseEntidade

class RestauranteEntidade(BaseEntidade):
    __tablename__ = 'Restaurantes'

    id = Column("pk_restaurantes", Integer, primary_key=True)
    nome = Column(String(100), unique=True)
    descricao = Column(UnicodeText, unique=False)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, descricao:str, data_insercao:Union[DateTime, None] = None):        
        self.nome = nome
        self.descricao = descricao

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
