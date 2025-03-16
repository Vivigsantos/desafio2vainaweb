from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.String(255), nullable=False)
    autor = db.Column(db.String(255), nullable=False)
    imagem_url = db.Column(db.String(500), nullable=False)


# Criar o banco de dados
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return "Bem-vindo à API de Livros! Doe um livro e ajude a espalhar conhecimento."


@app.route('/doar', methods=['POST'])
def doar_livro():
    dados = request.get_json()
    novo_livro = Livro(
        titulo=dados['titulo'],
        categoria=dados['categoria'],
        autor=dados['autor'],
        imagem_url=dados['imagem_url']
    )
    db.session.add(novo_livro)
    db.session.commit()
    return jsonify({"mensagem": "Livro cadastrado com sucesso!"}), 201


@app.route('/livros', methods=['GET'])
def listar_livros():
    livros = Livro.query.all()
    resultado = [{
        "id": livro.id,
        "titulo": livro.titulo,
        "categoria": livro.categoria,
        "autor": livro.autor,
        "imagem_url": livro.imagem_url
    } for livro in livros]
    return jsonify(resultado)


if __name__ == '__main__':
    app.run(debug=True)
