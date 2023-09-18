from pydantic import BaseModel
from typing import Optional, List
from modelos.conta.conta_entidade import ContaEntidade

class ObterCardapioRestauranteSchema(BaseModel):
    id_restaurante: int = 123
 
class Item:
    def __init__(self, nome: str):
        self.nome = nome    

class CardapioSecao:
    def __init__(self, nome: str, item: Item):
        self.nome = nome    
        self.item = item

class ObterCardapioRestauranteViewSchema(BaseModel):
    id_restaurante: int = 123
    nome_restaurante: str = "Meu restaurante"    

    def __init__(self, id: int, nome: str, cardapio_secoes: list[CardapioSecao]):
        self.id = id
        self.nome = nome
        self.cardapio_secoes = cardapio_secoes









        
    
