from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  modelos.base.base_entidade import BaseEntidade

class ContaEntidade(BaseEntidade):
    __tablename__ = 'Contas'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), unique=True)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str):    
        self.nome = nome