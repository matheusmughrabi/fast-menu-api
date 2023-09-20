from pydantic import BaseModel
from typing import Optional, List
from modelos.conta.conta_entidade import ContaEntidade
from typing import List

class ObterCardapioRestauranteSchema(BaseModel):
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

class ObterCardapioRestauranteViewSchema(BaseModel):
    id_restaurante: int
    nome_restaurante: str
    cardapio: Cardapio
    cardapio_secoes: List[CardapioSecao]








        
    
