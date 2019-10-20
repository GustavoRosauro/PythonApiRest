from flask import Flask, request, Response, jsonify
import json
from PessoaDAO import mostrarPessoas,inserirPessoa
from pessoa import Pessoa

app = Flask(__name__)

@app.route('/')
def index():
    response = Response(json.dumps(mostrarPessoas()), mimetype="application/json")
    return response
@app.route('/save', methods=['POST'])
def save():
    try:
        """pessoa = {
            "nome": request.json['nome'],
            "idade": request.json['idade'],
            "cpf": request.json['cpf']
        }"""
        pessoa = Pessoa(request.json['nome'], request.json['idade'], request.json['cpf'])
        inserirPessoa(pessoa)
        resp = jsonify("Inseridos com sucesso")
        return resp
    except print(Exception):
        pass