from flask import Flask, redirect, jsonify
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.orm import joinedload
from fastapi import HTTPException, Depends, FastAPI
from fastapi.responses import JSONResponse

from modelos import *
from schemas import *
from bootstrapper.inicializador_db import seed_data
from controllers.restaurante_controller import register_restaurante_routes
from controllers.cardapio_controller import registrar_cardapio_rotas
from controllers.cardapio_secao_controller import registrar_cardapio_secao_rotas

# Carga inicial da aplicação
seed_data()

info = Info(title="Fast Menu Api", version="1.0.0", description="Fast Menu Api contém as rotas para manutenção do cardápio de um restaurante")
app = OpenAPI(__name__, info=info)
CORS(app)


register_restaurante_routes(app)
registrar_cardapio_rotas(app)
registrar_cardapio_secao_rotas(app)

@app.route('/')
def redirect_to_swagger():
    return redirect('/openapi/swagger')


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
        
    app.run(HOST, PORT)
