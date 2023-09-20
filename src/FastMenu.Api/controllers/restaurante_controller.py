from flask_openapi3 import OpenAPI, Info, Tag

from modelos import *
from schemas import *

restaurante_tag = Tag(name="Restaurante")

def register_restaurante_routes(app: OpenAPI):
    @app.get('/restaurante/home', tags=[restaurante_tag], responses={"200": ObterCardapioRestauranteViewSchema, "404": ErrorSchema})
    def get_produto(query: ObterCardapioRestauranteSchema):
        session = Session()
    
        restaurante = session.query(RestauranteEntidade).filter_by(id=query.id_restaurante).one_or_none()
        if not restaurante:
            raise ValueError(f"Restaurante com ID {query.id_restaurante} não encontrado")

        cardapio = restaurante.cardapio

        cardapio_secoes = []
        for secao_entidade in cardapio.secoes:
            itens = []
            for item_entidade in secao_entidade.itens:
                item = Item(id_item=item_entidade.id,nome=item_entidade.nome, valor=item_entidade.valor)
                itens.append(item)
            cardapio_secao = CardapioSecao(id_cardapio_secao=secao_entidade.id,nome=secao_entidade.nome, itens=itens)
            cardapio_secoes.append(cardapio_secao)

        cardapio_view = ObterCardapioRestauranteViewSchema(
            id_restaurante=restaurante.id,
            nome_restaurante=restaurante.nome,
            cardapio= Cardapio(id_cardapio = cardapio.id),
            cardapio_secoes=cardapio_secoes
        )

        return cardapio_view.dict()
