from pydantic import BaseModel

class AtualizarCardapioSecaoNomeSchema(BaseModel):
    id_secao: int
    nome: str