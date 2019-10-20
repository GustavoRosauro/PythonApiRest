import mysql.connector
from pessoa import Pessoa

db = mysql.connector.connect(host="localhost", database="empresa", user="root", password="",)

def mostrarPessoas():
    cusror = db.cursor()
    listaPessoas = list()
    sqlSelet = "SELECT NOME,IDADE,CPF FROM PESSOA"
    cusror.execute(sqlSelet)
    resutado = cusror.fetchall()
    return {"pessoas": resutado}


