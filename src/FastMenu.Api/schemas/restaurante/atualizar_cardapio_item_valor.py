from pydantic import BaseModel

class AtualizarCardapioItemValorSchema(BaseModel):
    id: int
    valor: float