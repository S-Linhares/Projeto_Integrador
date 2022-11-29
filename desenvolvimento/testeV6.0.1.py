from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def raiz():
    preenchendo = 0
    return render_template('index.html', pr=preenchendo)


@app.route('/resultado', methods=['GET'])  # method informa os metodos aceitaveis nesta rota
def resultado():
    preenchendo = 1
    cidade_destino = int(request.args.get('nome_destino'))  # Se for usado "post", se troca o "args" por "form"
    cidade_inicio = request.args.get('nome_inicio')
    return render_template('index.html', ci='A partir daqui você vai ir de cavalo!', cd=cidade_destino, pr=preenchendo)
    # return f'destino: {cidade_destino}\ninicio: {cidade_inicio}'


app.run(debug=True)
