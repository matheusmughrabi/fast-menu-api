from sqlalchemy import Column, String, Integer, DateTime, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  modelos.base.base_entidade import BaseEntidade

'''
A seção de um cardápio tem como objetivo organizar o ítens servidos no restaurante de forma a melhorar a disposição do cardápio.
Toda seção pertence a um cardápio e possui N ítens associados a ela.
'''
class CardapioSecaoEntidade(BaseEntidade):
    __tablename__ = 'CardapioSecao'

    id = Column(Integer, primary_key=True)
    _nome = Column('nome', String(100), unique=True)
    _id_cardapio = Column('id_cardapio', Integer, ForeignKey('Cardapios.id'), nullable=False)
    data_insercao = Column(DateTime, default=datetime.now())

    itens = relationship("CardapioItemEntidade", backref="secao", cascade="all, delete-orphan")

    def __init__(self, nome:str, id_cardapio:int):        
        self.nome = nome
        self.id_cardapio = id_cardapio
     
    # Getter and Setter for nome
    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, value: str):
        if not value:
            raise ValueError("O nome não pode ser vazio")
        self._nome = value    
        
     # Getter and Setter for id_cardapio
    @property
    def id_cardapio(self) -> int:
        return self._id_cardapio

    @id_cardapio.setter
    def id_cardapio(self, value: int):
        self._id_cardapio = value

    def adicionarItemCardapio(self, item):
        # Verificando se já existe um item com o mesmo nome
        for existente_item in self.itens:
            if existente_item.nome == item.nome:
                raise ValueError(f"Já existe um item com o nome '{item.nome}' nesta seção.")

        self.itens.append(item)
