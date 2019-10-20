from flask import Flask, request, Response
import json
from PessoaDAO import mostrarPessoas

app = Flask(__name__)

@app.route('/')
def index():
    response = Response(json.dumps(mostrarPessoas()), mimetype="application/json")
    return response