from sqlalchemy import Column, String, Integer, DateTime, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  modelos.base.base_entidade import BaseEntidade

'''
Esta é a entidade raiz dos restaurantes da aplicação.
Ela tem relação com cardápio, o que retrata bem o mundo real (cada restaurante possui um cardápio)
Atualmente cada restaurante só possui 1 único cardápio
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
