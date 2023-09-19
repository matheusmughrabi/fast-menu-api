from pydantic import BaseModel

class AtualizarCardapioItemNomeSchema(BaseModel):
    id: int
    nome: str