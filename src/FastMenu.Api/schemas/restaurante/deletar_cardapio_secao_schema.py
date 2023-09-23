from pydantic import BaseModel

class DeletarCardapioSecaoSchema(BaseModel):
    '''
    Define como uma seção do cardápio deve ser deletada
    '''
    id_secao: int