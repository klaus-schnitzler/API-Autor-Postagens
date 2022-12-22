from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
 
def create_app():
    # Criar um API
    app = Flask(__name__)
 
    with app.app_context():
        # Criar uma instância de SQLAlchemy
        app.config['SECRET_KEY'] = 'FJk@2NmyTk4b8HJkAXCxlajKkn4'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
        db = SQLAlchemy(app)
        db: SQLAlchemy
 
 
        #id_postagem, titulo, autor
        # Definir a estrutura da tabela postagem
        class Postagem(db.Model):
            __tablename__ = 'postagem'
            id_postagem = db.Column(db.Integer, primary_key=True)
            titulo = db.Column(db.String)
            id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))
 
            #autor = db.Column(db.String)
 
        # Definir a estrutura da tabela Autor
        #id_autor, nome, email, senha, admin, postagens
 
 
        class Autor(db.Model):
            __tablename__ = 'autor'
            id_autor = db.Column(db.Integer, primary_key=True)
            nome = db.Column(db.String)
            email = db.Column(db.String)
            senha = db.Column(db.String)
            admin = db.Column(db.Boolean)
            postagens = db.relationship('Postagem')
 
 
        # Executar o comando para criar o banco de dados
        db.drop_all()
        db.create_all()
 
        # Criar usuários administradores
        autor = Autor(nome='claudio', email='fatorandoamatematica@gmail.com',
                    senha='123456', admin=True)
 
        db.session.add(autor)
        db.session.commit()
       
        return app
 
create_app()