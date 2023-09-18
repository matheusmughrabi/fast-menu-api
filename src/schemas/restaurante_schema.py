from pydantic import BaseModel
from typing import Optional, List
from modelos.restaurante.restaurante_entidade import RestauranteEntidade



class CriarRestauranteSchema(BaseModel):
    """ Define como um novo restaurante deve ser criado
    """
    nome: str = "Meu restaurante"
    descricao: str = "Uma descrição qualquer"

class DeletarRestauranteSchema(BaseModel):
    "Define como um restaurante deve ser deletado"
    id: int = 123