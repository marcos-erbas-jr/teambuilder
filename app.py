from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/construcao.html")
def construcao():
    return render_template('construcao.html')

@app.route("/equipes.html")
def teams():
    return render_template('equipes.html')

@app.route("/inscricao.html")
def inscricao():
    return render_template('inscricao.html')

@app.route("/projetos.html")
def projects():
    return render_template('projetos.html')

@app.route("/proposta.html")
def proposta():
    return render_template('proposta.html')

@app.route("/ranking.html")
def rank():
    return render_template('ranking.html')

@app.route("/sobre.html")
def sobre():
    return render_template('sobre.html')

@app.route("/vagas.html")
def vagas():
    return render_template('vagas.html')

if __name__ == '__main__':
    app.run(debug=True)