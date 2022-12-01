from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def raiz():
    return render_template('index.html')


@app.route('/resultado', methods=['GET', 'POST'])  # method informa os metodos aceitaveis nesta rota
def resultado():
    cidade_destino = int(request.form.get('nome_destino'))  # Se for usado "post", se troca o "args" por "form"
    cidade_inicio = int(request.form.get('nome_inicio'))
    transporte_escolhido = int(request.form.get('transporte'))
    fdp = [{'atual': 'passeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeei', 'final': 'pro', 'trans': 'cuzin'},
           {'atual': '---passei\n', 'final': 'pro', 'trans': 'pintin'},
           {'atual': 'passei', 'final': 'pro', 'trans': 'peitin'}]
    fdp2 = list()
    fdp2.append(fdp)
    return render_template('index.html', fdp2=fdp2)
    # return f'destino: {cidade_destino}\ninicio: {cidade_inicio}'


app.run(debug=True)
