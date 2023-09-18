from pydantic import BaseModel
from typing import Optional, List
from modelos.contas.conta_entidade import ContaEntidade

class CriarContaSchema(BaseModel):
    """ Define como uma nova conta deve ser criada na aplicação
    """
    nome_conta: str = "Minha franquia"
    nome_responsavel: str = "João"
    cpf_responsavel: str = "000.000.000-00"
    email_responsavel: str = "joao@example.com"
    senha_responsavel: str = "123!senha?muito_dificil"

class DeletarContaSchema(BaseModel):
    """ Define como uma nova conta deve ser deletada na aplicação
    """
    id: str = 123