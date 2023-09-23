from sqlalchemy import Column, String, Integer, DateTime, UnicodeText, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  modelos.base.base_entidade import BaseEntidade

'''
Cada item do cardápio é um prato servido pelo restaurante.
Todo item pertence a uma seção do cardápio.
'''
class CardapioItemEntidade(BaseEntidade):
    __tablename__ = 'CardapioItem'

    id = Column('id', Integer, primary_key=True)
    _nome = Column('nome', String(100), nullable=False, unique=False)
    _valor = Column('valor', Float, nullable=False, unique=False)
    _id_cardapio_secao = Column('id_cardapio_secao', Integer, ForeignKey('CardapioSecao.id'), nullable=False)
    _data_insercao = Column('data_insercao', DateTime, default=datetime.now())

    def __init__(self, nome:str, valor:float, id_cardapio_secao: int):
        self.nome = nome
        self.valor = valor
        self.id_cardapio_secao = id_cardapio_secao

    # Getters and Setters for nome
    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        if not nome:
            raise ValueError("O nome não pode ser vazio")
        self._nome = nome

    # Getters and Setters for valor
    @property
    def valor(self) -> float:
        return self._valor
    
    @valor.setter
    def valor(self, value: float):
        if value < 0:
            raise ValueError("O valor não pode ser negativo")
        self._valor = value

    # Getters and Setters for id_cardapio_secao
    @property
    def id_cardapio_secao(self) -> int:
        return self._id_cardapio_secao

    @id_cardapio_secao.setter
    def id_cardapio_secao(self, value: int):
        self._id_cardapio_secao = value

    @property
    def data_insercao(self) -> datetime:
        return self._data_insercao
