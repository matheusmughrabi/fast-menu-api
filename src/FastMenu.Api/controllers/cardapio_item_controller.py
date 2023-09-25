from flask import jsonify
from flask_openapi3 import OpenAPI, Tag

from modelos import *
from schemas import *

cardapio_item_tag = Tag(name="Cardapio Item", description="O controller Cardápio Item contém rotas para gerenciar os ítens de cada seção do cardápio")

def registrar_cardapio_item_rotas(app: OpenAPI):
    @app.post('/cardapio-item/novo', tags=[cardapio_item_tag], responses={"201": None, "409": ErrorSchema, "404": ErrorSchema, "400": ErrorSchema})
    def add_cardapio_item(form: AdicionarCardapioItemSchema):
        session = Session()

        try:
            # Validação de falha rápida
            item_exists = session.query(
                    session.query(CardapioItemEntidade)
                    .filter_by(_nome=form.nome, _id_cardapio_secao=form.id_cardapio_secao)
                    .exists()
                ).scalar()

            if item_exists:
                return jsonify({"message": f"Já existe um item com o nome '{form.nome}' nesta seção."}), 409            

            secao = session.query(CardapioSecaoEntidade).filter_by(id=form.id_cardapio_secao).one_or_none()

            if not secao:
                return jsonify({"message": "id_cardapio_secao não existe"}), 404

            new_item = CardapioItemEntidade(
                nome=form.nome,
                valor=form.valor,
                id_cardapio_secao=form.id_cardapio_secao
            )    

            try:
                secao.adicionarItemCardapio(new_item)
            except ValueError as e:
                return jsonify({"message": str(e)}), 400

            session.commit()

            return jsonify({}), 201
    
        finally:
            session.close()

    @app.patch('/cardapio-item/atualizar-valor', tags=[cardapio_item_tag], responses={"200": None, "404": ErrorSchema, "400": ErrorSchema})
    def update_cardapio_item_value(form: AtualizarCardapioItemValorSchema):
        session = Session()

        try:
            cardapio_item = session.query(CardapioItemEntidade).filter_by(id=form.id).one_or_none()

            if not cardapio_item:
                return jsonify({"message": "cardapio_item não encontrado"}), 404

            cardapio_item.valor = form.valor
            session.commit()

            return jsonify({"message": "Valor do cardapio_item atualizado com sucesso!"}), 200

        except ValueError as ve:
            session.rollback()
            return jsonify({"message": str(ve)}), 400

        except Exception as e:
            session.rollback()
            return jsonify({"message": "Erro interno no servidor"}), 500

        finally:
            session.close()

    @app.patch('/cardapio-item/atualizar-nome', tags=[cardapio_item_tag], responses={"200": None, "409": ErrorSchema, "404": ErrorSchema, "400": ErrorSchema})
    def update_cardapio_item_nome(form: AtualizarCardapioItemNomeSchema):
        session = Session()

        try:
            cardapio_item = session.query(CardapioItemEntidade).filter_by(id=form.id).one_or_none()

            if not cardapio_item:
                return jsonify({"message": "cardapio_item não encontrado"}), 404

                        # Validação de falha rápida
            # TODO: Extrair um método para reutilizar esta query, pois está sendo utilizada em dois lugares
            item_exists = session.query(
                        session.query(CardapioItemEntidade)
                        .filter_by(_nome=form.nome, _id_cardapio_secao=cardapio_item.id_cardapio_secao)
                        .exists()
                    ).scalar()

            if item_exists:
                return jsonify({"message": f"Já existe um item com o nome '{form.nome}' nesta seção."}), 409              

            cardapio_item.nome = form.nome
            session.commit()

            return jsonify({"message": "Nome do cardapio_item atualizado com sucesso!"}), 200

        except ValueError as ve:
            session.rollback()
            return jsonify({"message": str(ve)}), 400

        except Exception as e:
            session.rollback()
            return jsonify({"message": "Erro interno no servidor"}), 500

        finally:
            session.close()

    @app.delete('/cardapio-item/deletar', tags=[cardapio_item_tag], responses={"200": None, "404": ErrorSchema, "400": ErrorSchema})
    def delete_cardapio_item(form: DeletarCardapioItemSchema):
        session = Session()

        try:
            cardapio_item = session.query(CardapioItemEntidade).filter_by(id=form.id_cardapio_item).one_or_none()

            if not cardapio_item:
                return jsonify({"message": "cardapio_item não encontrado"}), 404

            session.delete(cardapio_item)
            session.commit()

            return jsonify({"message": "Cardapio item deletado com sucesso!"}), 200

        except ValueError as ve:
            session.rollback()
            return jsonify({"message": str(ve)}), 400

        except Exception as e:
            session.rollback()
            return jsonify({"message": "Erro interno no servidor"}), 500

        finally:
            session.close()