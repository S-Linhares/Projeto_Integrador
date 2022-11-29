from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def raiz():
    return 'Olá, mundo!'


@app.route('/rota2')
def rota2():
    return '<H1> Essa é a segunda rota da aplicação!</H1>'


@app.route('/pessoa/<string:nome>/<string:cidade>')
def pessoa(nome, cidade):
    return jsonify({'nome': nome, 'cidade': cidade})


app.run(debug=True)
