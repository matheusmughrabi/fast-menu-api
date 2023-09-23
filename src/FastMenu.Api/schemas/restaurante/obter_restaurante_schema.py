from pydantic import BaseModel
from typing import Optional, List
from modelos.conta.conta_entidade import ContaEntidade
from typing import List

class ObterCardapioRestauranteSchema(BaseModel):
    '''
    Define o payload necessário para obter o cardápio de um restaurante
    '''
    id_restaurante: int = 123

class Item(BaseModel):
    id_item: int
    nome: str
    valor: float

class CardapioSecao(BaseModel):
    id_cardapio_secao: int
    nome: str
    itens: List[Item]
    
class Cardapio(BaseModel):
    id_cardapio: int
    cardapio_secoes: List[CardapioSecao]

class ObterCardapioRestauranteViewSchema(BaseModel):
    '''
    Define o retorno com os dados do cardápio de um restaurante
    '''
    id_restaurante: int
    nome_restaurante: str
    cardapio: Cardapio









        
    
