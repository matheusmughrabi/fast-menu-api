from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

from modelos.base.base_entidade import BaseEntidade
from modelos.conta.conta_entidade import ContaEntidade
from modelos.restaurante.restaurante_entidade import RestauranteEntidade
from modelos.restaurante.cardapio_entidade import CardapioEntidade
from modelos.restaurante.cardapio_secao_entidade import  CardapioSecaoEntidade
from modelos.restaurante.cardapio_item_entidade import CardapioItemEntidade

'''
Aqui vamos criar o banco de dados sqlite dentro do diretório database.
Também vamos criar as tabelas do banco.
'''
caminho_banco = "database/"
if not os.path.exists(caminho_banco):
   os.makedirs(caminho_banco)

url_banco = 'sqlite:///%s/db.sqlite3' % caminho_banco

engine = create_engine(url_banco, echo=False)

Session = sessionmaker(bind=engine)

if not database_exists(engine.url):
    create_database(engine.url) 

BaseEntidade.metadata.create_all(engine)
