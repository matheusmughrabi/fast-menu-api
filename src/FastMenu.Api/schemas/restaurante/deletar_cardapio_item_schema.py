from pydantic import BaseModel

class DeletarCardapioItemSchema(BaseModel):
    '''
    Define como um item do cardápio deve ser deletado
    '''
    id_cardapio_item: int = 1