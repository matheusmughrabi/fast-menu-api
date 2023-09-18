from functools import cached_property
from flask import Flask, redirect
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag

from modelos import *
from schemas import *

def seed_data():
    session = Session()
    
    if session.query(ContaEntidade).count() > 0:
        return


    conta = ContaEntidade("Minha franquia")
    session.add(conta)
    session.flush()
    
    usuario = UsuarioEntidade("João Silva", "000.000.000-00", "joao@exemplo.com", "12345", conta.id)
    session.add(usuario)
    session.flush()
    
    restaurante = RestauranteEntidade("Meu restaurante", "Meu restaurante desc", conta.id)
    session.add(restaurante)
    session.flush()
    
    cardapio = CardapioEntidade(restaurante.id)
    session.add(cardapio)
    session.flush()  
    
    cardapio_secao_pratos_principais = CardapioSecaoEntidade("Pratos principais", cardapio.id)
    cardapio_secao_sobremesas = CardapioSecaoEntidade("Sobremesas", cardapio.id)
    session.add(cardapio_secao_pratos_principais)
    session.add(cardapio_secao_sobremesas)
    session.flush()   
    
    cardapio_item_1 = CardapioItemEntidade("Macarrão molho branco", 50, cardapio_secao_pratos_principais.id)
    cardapio_item_2 = CardapioItemEntidade("Pizza", 90, cardapio_secao_pratos_principais.id)
    cardapio_item_3 = CardapioItemEntidade("Risoto", 75, cardapio_secao_pratos_principais.id)
    cardapio_item_4 = CardapioItemEntidade("Sorvete", 15, cardapio_secao_sobremesas.id)
    cardapio_item_5 = CardapioItemEntidade("Brownie", 18, cardapio_secao_sobremesas.id)
    cardapio_item_6 = CardapioItemEntidade("Cholocate", 10, cardapio_secao_sobremesas.id)
    
    session.add(cardapio_item_1)
    session.add(cardapio_item_2)
    session.add(cardapio_item_3)
    session.add(cardapio_item_4)
    session.add(cardapio_item_5)
    session.add(cardapio_item_6)
    
    session.commit()

    
    