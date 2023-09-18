from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  modelos.base.base_entidade import BaseEntidade

class UsuarioEntidade(BaseEntidade):
    __tablename__ = 'Usuarios'

    id = Column("pk_usuarios", Integer, primary_key=True)
    nome = Column(String(100), unique=True)
    cpf = Column(String(100), unique=True)
    email = Column(String(100), unique=True)
    senhaHash = Column(String(500), unique=True)
    id_conta = Column(Integer, ForeignKey('Contas.pk_contas'), nullable=False)
    data_insercao = Column(DateTime, default=datetime.now())

    conta = relationship("ContaEntidade", back_populates="responsavel", foreign_keys=[id_conta])

    def __init__(self, nome:str, cpf:str, email:str, senhaHash:str, id_conta: int, data_insercao:Union[DateTime, None] = None):        
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senhaHash = senhaHash
        self.id_conta = id_conta

        if data_insercao:
            self.data_insercao = data_insercao