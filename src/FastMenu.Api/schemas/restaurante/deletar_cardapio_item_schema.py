from pydantic import BaseModel

class DeletarCardapioItemSchema(BaseModel):
    '''
    Define como um ítem do cardápio deve ser deletado
    '''
    id_cardapio_item: int = 1