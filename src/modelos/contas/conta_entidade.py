from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  modelos.base.base_entidade import BaseEntidade

class ContaEntidade(BaseEntidade):
    __tablename__ = 'Contas'

    id = Column("pk_contas", Integer, primary_key=True)
    nome = Column(String(100), unique=True)
    id_responsavel_principal = Column(Integer, nullable=False, unique=True)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, id_reponsavel_principal:int, data_insercao:Union[DateTime, None] = None):    
        self.nome = nome
        self.id_reponsavel_principal = id_reponsavel_principal
        
        if data_insercao:
            self.data_insercao = data_insercao
