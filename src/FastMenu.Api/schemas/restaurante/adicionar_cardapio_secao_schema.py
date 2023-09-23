from pydantic import BaseModel

class AdicionarCardapioSecaoSchema(BaseModel):
    '''
    Define como uma seção do cardápio deve ser criada
    '''
    nome: str = "Pratos principais"
    id_cardapio: int = 1