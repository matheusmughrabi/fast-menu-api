from pydantic import BaseModel

class AtualizarCardapioItemValorSchema(BaseModel):
    '''
    Define como o valor de um item do cardápio deve ser atualizado
    '''
    id: int = 1
    valor: float = 20.00