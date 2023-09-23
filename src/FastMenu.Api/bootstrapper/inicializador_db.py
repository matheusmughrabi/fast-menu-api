from functools import cached_property
from flask import Flask, redirect
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag

from modelos import *
from schemas import *

'''
Neste método criei uma pequena carga no banco de dados, pois ainda não temos o módulo de criação de contas implementado.
Quando a aplicação tiver o módulo de criação de contas implementado, esse método deixará de existir
'''
def inicializar():
    sessao = Session()
    
    # Apenas uma verificação para que o banco seja inicializado uma única vez
    if sessao.query(ContaEntidade).count() > 0:
        return


    conta = ContaEntidade("Minha franquia")
    sessao.add(conta)
    sessao.flush()
    
    restaurante = RestauranteEntidade("Meu restaurante", "Meu restaurante desc", conta.id)
    sessao.add(restaurante)
    sessao.flush()
    
    cardapio = CardapioEntidade(restaurante.id)
    sessao.add(cardapio)
    sessao.flush()  
    
    cardapio_secao_pratos_principais = CardapioSecaoEntidade("Pratos principais", cardapio.id)
    cardapio_secao_sobremesas = CardapioSecaoEntidade("Sobremesas", cardapio.id)
    sessao.add(cardapio_secao_pratos_principais)
    sessao.add(cardapio_secao_sobremesas)
    sessao.flush()   
    
    cardapio_item_1 = CardapioItemEntidade("Macarrão molho branco", 50, cardapio_secao_pratos_principais.id)
    cardapio_item_2 = CardapioItemEntidade("Pizza", 90, cardapio_secao_pratos_principais.id)
    cardapio_item_3 = CardapioItemEntidade("Risoto", 75, cardapio_secao_pratos_principais.id)
    cardapio_item_4 = CardapioItemEntidade("Sorvete", 15, cardapio_secao_sobremesas.id)
    cardapio_item_5 = CardapioItemEntidade("Brownie", 18, cardapio_secao_sobremesas.id)
    cardapio_item_6 = CardapioItemEntidade("Cholocate", 10, cardapio_secao_sobremesas.id)
    
    sessao.add(cardapio_item_1)
    sessao.add(cardapio_item_2)
    sessao.add(cardapio_item_3)
    sessao.add(cardapio_item_4)
    sessao.add(cardapio_item_5)
    sessao.add(cardapio_item_6)
    
    sessao.commit()

    
    