from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importando os elementos definidos no modelo
from modelos.base.base_entidade import BaseEntidade
from modelos.conta.conta_entidade import ContaEntidade
from modelos.conta.usuario_entidade import UsuarioEntidade
from modelos.restaurante.restaurante_entidade import RestauranteEntidade
from modelos.restaurante.cardapio_entidade import CardapioEntidade
from modelos.restaurante.cardapio_secao_entidade import  CardapioSecaoEntidade
from modelos.restaurante.cardapio_item_entidade import CardapioItemEntidade

db_path = "database/"
# Verifica se o diretorio não existe
if not os.path.exists(db_path):
   # então cria o diretorio
   os.makedirs(db_path)

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir 
if not database_exists(engine.url):
    create_database(engine.url) 

# cria as tabelas do banco, caso não existam
BaseEntidade.metadata.create_all(engine)
