from pydantic import BaseModel

class AdicionarCardapioItemSchema(BaseModel):
    '''
    Define como um novo item do cardápio deve ser criado
    '''
    nome: str = "Arroz"
    valor: float = 15.99
    id_cardapio_secao: int = 1
