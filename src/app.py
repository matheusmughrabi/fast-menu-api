from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from flask import Flask, redirect

from modelos import *
from modelos import Session
from schemas import *

app = Flask(__name__)

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
produto_tag = Tag(name="Produto", description="Adição, visualização e remoção de produtos à base")

@app.post('/conta/novo', tags=[produto_tag],
          responses={"200": CriarContaSchema, "409": ErrorSchema, "400": ErrorSchema})
def criar_conta(form: CriarContaSchema):
    """ Cria uma conta no aplicativo
    """
    session = Session()
    conta = ContaEntidade(nome=form.nome_conta)
    session.add(conta)
    session.flush()  # Garante que a conta é inserida e obtém o ID gerado

    # Criar a entidade do usuário (responsável pela conta)
    usuario = UsuarioEntidade(
        nome=form.nome_responsavel,
        cpf=form.cpf_responsavel,
        email=form.email_responsavel,
        senhaHash=form.senha_responsavel,  # No mundo real, você deve hashear a senha
        id_conta=conta.id
    )
    session.add(usuario)

    # Associar o usuário como responsável principal da conta
    conta.id_responsavel_principal = usuario.id
    session.flush()

    session.commit()  # Confirma as operações no banco

    return "restaurante criado", 200

@app.delete('/conta', tags=[produto_tag],
          responses={"200": DeletarContaSchema, "409": ErrorSchema, "400": ErrorSchema})
def deletar_conta(form: DeletarContaSchema):
    """ Deleta uma conta no aplicativo
    """

    session = Session()
    count = session.query(ContaEntidade).filter(ContaEntidade.id == form.id).delete()
    session.commit()

    return "conta deletada", 200

@app.post('/restaurante/novo', tags=[produto_tag],
          responses={"200": CriarRestauranteSchema, "409": ErrorSchema, "400": ErrorSchema})
def criar_restaurante(form: CriarRestauranteSchema):
    """ Cria um restaurante dentro de uma conta no aplicativo
    """
    restaurante = RestauranteEntidade(
        nome=form.nome,
        descricao=form.descricao)

    # criando conexão com a base
    session = Session()
    # adicionando produto
    session.add(restaurante)
    # efetivando o camando de adição de novo item na tabela
    session.commit()
    return "restaurante criado", 200

@app.delete('/restaurante', tags=[produto_tag],
          responses={"200": DeletarRestauranteSchema, "409": ErrorSchema, "400": ErrorSchema})
def deletar_restaurante(form: DeletarRestauranteSchema):
    """ Deleta um restaurante dentro de uma conta no aplicativo
    """

    # criando conexão com a base
    session = Session()
    # adicionando produto
    count = session.query(RestauranteEntidade).filter(RestauranteEntidade.id == form.id).delete()
    # efetivando o camando de adição de novo item na tabela
    session.commit()
    return "restaurante deletado", 200

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

