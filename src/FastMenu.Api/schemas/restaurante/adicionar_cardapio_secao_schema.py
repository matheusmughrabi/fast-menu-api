from pydantic import BaseModel

class AdicionarCardapioSecaoSchema(BaseModel):
    nome: str
    id_cardapio: int