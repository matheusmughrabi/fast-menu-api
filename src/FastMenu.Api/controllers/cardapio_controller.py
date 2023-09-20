from flask import jsonify
from flask_openapi3 import OpenAPI, Tag

from modelos import *
from schemas import *

cardapio_tag = Tag(name="Cardapio")

def registrar_cardapio_rotas(app: OpenAPI):
    @app.post('/menu-secao/novo', tags=[cardapio_tag], responses={"201": None, "409": ErrorSchema, "400": ErrorSchema})
    def adicionar_menu_secao(form: AdicionarCardapioSecaoSchema):
        session = Session() 
    
        try:
            cardapio = session.query(CardapioEntidade).filter_by(id=form.id_cardapio).one_or_none()

            if not cardapio:
                return jsonify({"detail": "id_cardapio não existe"}), 400

            nova_secao = CardapioSecaoEntidade(nome=form.nome, id_cardapio=form.id_cardapio)
        
            cardapio.adicionar_secao(nova_secao)
        
            session.commit()

            return jsonify({}), 201

        except ValueError as ve:
            session.rollback()
            return jsonify({"detail": str(ve)}), 409
    
        except Exception as e:
            session.rollback()
            return jsonify({"detail": "Erro interno no servidor"}), 500

        finally:
            session.close()


    @app.patch('/menu-secao/atualizar-nome', tags=[cardapio_tag], responses={"200": None, "404": ErrorSchema, "400": ErrorSchema})
    def update_menu_secao_nome(form: AtualizarCardapioSecaoNomeSchema):
        session = Session()

        # Buscar a seção do cardápio pelo ID fornecido
        secao = session.query(CardapioSecaoEntidade).filter_by(id=form.id_secao).one_or_none()
    
        if not secao:
            return jsonify({"detail": "id_secao não encontrado"}), 404

        secao.nome = form.nome    
        session.commit()
    
        return jsonify({}), 200


    @app.delete('/menu-secao/deletar', tags=[cardapio_tag], responses={"200": None, "404": ErrorSchema})
    def delete_menu_section(form: DeletarCardaptioSecaoSchema):
        session = Session()

        secao = session.query(CardapioSecaoEntidade).filter_by(id=form.id_secao).one_or_none()
    
        if not secao:
            return jsonify({"detail": "id_secao não encontrado"}), 404

        session.delete(secao)
        session.commit()
    
        return jsonify({}), 200
