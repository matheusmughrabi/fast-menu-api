from sqlalchemy import Column, String, Integer, DateTime, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  modelos.base.base_entidade import BaseEntidade

'''
A entidade restaurante possibilita que guardar os dados de um ou mais restaurantes que uma conta pode ter.
Todo e qualquer restaurante deve pertencer a uma conta.
Cada restaurante possui um cardápio no qual é possível que criar o ítens servidos no local.
'''
class RestauranteEntidade(BaseEntidade):
    __tablename__ = 'Restaurantes'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), unique=True)
    descricao = Column(UnicodeText, unique=False)
    id_conta = Column(Integer, ForeignKey('Contas.id'), nullable=False)
    data_insercao = Column(DateTime, default=datetime.now())

    cardapio = relationship("CardapioEntidade", backref="restaurante", uselist=False)
    
    def __init__(self, nome:str, descricao:str, id_conta: int):        
        self.nome = nome
        self.descricao = descricao
        self.id_conta = id_conta
