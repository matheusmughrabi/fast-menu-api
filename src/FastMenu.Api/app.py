from flask import Flask, redirect
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag

from modelos import *
from schemas import *
from bootstrapper.inicializador_db import seed_data

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
produto_tag = Tag(name="Produto", description="Adição, visualização e remoção de produtos à base")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.get('/restaurante/home', tags=[produto_tag],
         responses={"200": ObterCardapioRestauranteViewSchema, "404": ErrorSchema})
def get_produto(query: ObterCardapioRestauranteSchema):
    
    return "teste", 404

@app.post('/conta/novo', tags=[produto_tag], responses={"200": CriarContaSchema, "409": ErrorSchema, "400": ErrorSchema})
def criar_conta(form: CriarContaSchema):
    """ Cria uma conta no aplicativo
    """
    conta = ContaEntidade(nome=form.nome_conta)
    
    session = Session()
    session.add(conta)
    session.flush() 

    usuario = UsuarioEntidade(
        nome=form.nome_responsavel,
        cpf=form.cpf_responsavel,
        email=form.email_responsavel,
        senhaHash=form.senha_responsavel, 
        id_conta=conta.id
    )
    
    session.add(usuario)
    session.commit()

    return "conta criada", 200

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
        
    seed_data()
    app.run(HOST, PORT)
