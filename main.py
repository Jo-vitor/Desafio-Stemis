from flask import Flask, make_response, jsonify, request
import os
import mysql.connector

conexao = mysql.connector.connect(host=os.getenv("MYSQLHOST", default='localhost'), database=os.getenv("MYSQLDATABASE", default='desafioStemis'), user=os.getenv("MYSQLUSER", default='root'), password=os.getenv("MYSQLPASSWORD", default='123456'))

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False 

@app.route("/produtos", methods = ["GET"])
def get_produtos():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    tuplasprodutos = cursor.fetchall()

    listaprodutos = list()
    for produto in tuplasprodutos:
        listaprodutos.append(
            {
                "id do produto": produto[0],
                "nome": produto[1],
                "valor": produto[2],
                "quantidade em estoque": produto[3]
            }
        )

    return make_response(
        jsonify(
            mensagem = "Lista dos produtos em estoque",
            produtos = listaprodutos 
        )
    )

@app.route("/produtos/<id>", methods = ["GET"])
def get_produto(id):
    cursor = conexao.cursor()
    sql = f"SELECT * FROM produtos WHERE id_produto = {id}"
    cursor.execute(sql)
    pegaproduto = cursor.fetchone()

    umproduto = {
        "id do produto": pegaproduto[0],
        "nome": pegaproduto[1],
        "valor": pegaproduto[2],
        "quantidade em estoque": pegaproduto[3]
    }

    return make_response(
        jsonify(
            mensagem = "Produto selecionado",
            produto = umproduto
        )
    )

@app.route("/produtos", methods = ["POST"])
def create_produto():
    novoproduto = request.json

    cursor = conexao.cursor()
    sql = f"INSERT INTO produtos(nome, valor, quantidade) VALUES ('{novoproduto['nome']}', {novoproduto['valor']}, {novoproduto['quantidade em estoque']})"
    cursor.execute(sql)
    conexao.commit()

    return make_response(
        jsonify(
            mensagem = "Produto cadastrado com sucesso"
        )
    )

@app.route("/produtos/<id>", methods = ["PUT"])
def update_produto(id):
    atualizaestoque = request.json

    cursor = conexao.cursor()
    sql = f"UPDATE produtos SET quantidade = {atualizaestoque['quantidade em estoque']} WHERE id_produto = {id}"
    cursor.execute(sql)
    conexao.commit()

    return make_response(
        jsonify(
            mensagem = "Produto atulizado com sucesso"
        )
    )

@app.route("/produtos/<id>", methods = ["DELETE"])
def delete_produto(id):
    cursor = conexao.cursor()
    sql = f"DELETE FROM produtos WHERE id_produto = {id}"
    cursor.execute(sql)
    conexao.commit()

    return make_response(
        jsonify(
            mensagem = "Poduto deletado"
        )
    )

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("MYSQLPORT", default=5000))
