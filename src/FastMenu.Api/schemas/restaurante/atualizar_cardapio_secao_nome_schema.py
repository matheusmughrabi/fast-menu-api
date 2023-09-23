from pydantic import BaseModel

class AtualizarCardapioSecaoNomeSchema(BaseModel):
    '''
    Define como o nome de uma seção do cardápio deve estar atualizado
    '''
    id_secao: int = 1
    nome: str = "Pratos principais"