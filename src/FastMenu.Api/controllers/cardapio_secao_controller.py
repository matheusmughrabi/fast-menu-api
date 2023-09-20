from flask import jsonify
from flask_openapi3 import OpenAPI, Tag

from modelos import *
from schemas import *

cardapio_secao_tag = Tag(name="Cardapio Seção", description="O controller Cardápio Seção contém rotas para gerenciar os ítens de cada seção do cardápio")

def registrar_cardapio_secao_rotas(app: OpenAPI):
    @app.post('/cardapio-item/novo', tags=[cardapio_secao_tag], responses={"201": None, "409": ErrorSchema, "400": ErrorSchema})
    def add_cardapio_item(form: AdicionarCardapioItemSchema):
        session = Session()

        try:
            secao = session.query(CardapioSecaoEntidade).filter_by(id=form.id_cardapio_secao).one_or_none()

            if not secao:
                return jsonify({"detail": "id_cardapio_secao não existe"}), 400

            new_item = CardapioItemEntidade(
                nome=form.nome,
                valor=form.valor,
                id_cardapio_secao=form.id_cardapio_secao
            )    

            try:
                secao.adicionarItemCardapio(new_item)
            except ValueError as e:
                return jsonify({"detail": str(e)}), 409  # 409 indica um conflito, como um nome duplicado

            session.commit()

            return jsonify({}), 201
    
        finally:
            session.close()

    @app.patch('/cardapio-item/atualizar-valor', tags=[cardapio_secao_tag], responses={"200": None, "404": ErrorSchema, "400": ErrorSchema})
    def update_cardapio_item_value(form: AtualizarCardapioItemValorSchema):
        session = Session()
    
        cardapio_item = session.query(CardapioItemEntidade).filter_by(id=form.id).one_or_none()
        if not cardapio_item:
            return jsonify({"detail": "cardapio_item não encontrado"}), 404

        cardapio_item.valor = form.valor

        session.commit()

        return jsonify({"message": "Valor do cardapio_item atualizado com sucesso!"}), 200

    @app.patch('/cardapio-item/atualizar-nome', tags=[cardapio_secao_tag], responses={"200": None, "404": ErrorSchema, "400": ErrorSchema})
    def update_cardapio_item_nome(form: AtualizarCardapioItemNomeSchema):
        session = Session()
    
        cardapio_item = session.query(CardapioItemEntidade).filter_by(id=form.id).one_or_none()
        if not cardapio_item:
            return jsonify({"detail": "cardapio_item não encontrado"}), 404

        cardapio_item.nome = form.nome 

        session.commit()

        return jsonify({"message": "Nome do cardapio_item atualizado com sucesso!"}), 200

    @app.delete('/cardapio-item/deletar', tags=[cardapio_secao_tag], responses={"200": None, "404": ErrorSchema})
    def delete_cardapio_item(form: DeletarCardapioItemSchema):
        session = Session()
    
        # Encontrar o cardapio_item pelo seu ID.
        cardapio_item = session.query(CardapioItemEntidade).filter_by(id=form.id_cardapio_item).one_or_none()

        if not cardapio_item:
            return jsonify({"detail": "cardapio_item não encontrado"}), 404

        # Deletar o cardapio_item.
        session.delete(cardapio_item)
        session.commit()

        return jsonify({"message": "Cardapio item deletado com sucesso!"}), 200