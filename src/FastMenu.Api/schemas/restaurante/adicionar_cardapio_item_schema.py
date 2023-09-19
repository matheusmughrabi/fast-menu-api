from pydantic import BaseModel

class AdicionarCardapioItemSchema(BaseModel):
    nome: str
    valor: float
    id_cardapio_secao: int
