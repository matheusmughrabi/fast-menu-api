from sqlalchemy import Column, String, Integer, DateTime, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  modelos.base.base_entidade import BaseEntidade

class CardapioEntidade(BaseEntidade):
    __tablename__ = 'Cardapios'

    id = Column(Integer, primary_key=True)
    id_restaurante = Column(Integer, ForeignKey('Restaurantes.id'), nullable=False)
    data_insercao = Column(DateTime, default=datetime.now())

    secoes = relationship("CardapioSecaoEntidade", backref="cardapio")

    def __init__(self, id_restaurante:int):        
        self.id_restaurante = id_restaurante
        
    def adicionar_secao(self, secao):
        # Verificar se já existe uma seção com o mesmo nome
        for existente in self.secoes:
            if existente.nome == secao.nome:
                raise ValueError(f"Já existe uma seção com o nome '{secao.nome}' no cardápio.")
        # Se não existir, adicione à lista
        self.secoes.append(secao)