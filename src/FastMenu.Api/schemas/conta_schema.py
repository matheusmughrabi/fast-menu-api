from pydantic import BaseModel
from typing import Optional, List
from modelos.conta.conta_entidade import ContaEntidade

class CriarContaSchema(BaseModel):
    nome_conta: str = "Minha franquia"
    nome_responsavel: str = "Joao"
    cpf_responsavel: str = "000.000.000-00"
    email_responsavel: str = "joao@example.com"
    senha_responsavel: str = "123!senha?muito_dificil"

class DeletarContaSchema(BaseModel):
    """ Define como uma nova conta deve ser deletada na aplicacao
    """
    id: str = 123