from pydantic import BaseModel

class AtualizarCardapioItemNomeSchema(BaseModel):
    '''
    Define como o nome de um item do cardápio deve ser atualizado
    '''
    id: int = 1
    nome: str = "Arroz"