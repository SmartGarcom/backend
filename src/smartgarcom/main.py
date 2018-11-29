from model import db
from time import sleep
from core.endpoints import *
from flask import Flask
import os


# DB_URL = 'sqlite:///sqlite.sql'
DB_URL = 'postgres://kiyvntduclansh:d74c329141605a04226d9b98186504a598d62be508c9a78ee4b7c34591e18fe4@ec2-54-227-249-201.compute-1.amazonaws.com:5432/ddr8j5sopft0ed' 

app = Flask(__name__)
app.secret_key = os.urandom(64)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


from flask import current_app
with app.app_context():
    db.init_app(app)
    # db.drop_all()
    db.create_all()

from flask_restful import Resource, Api
api = Api(app)


class Estabelecimento(Resource):
    def get(self):
    	parser.add_argument('cnpj', type=str)
    	return Empresa.query.filter_by(**parser.parse_args()).first()

    def put(self):
    	parser = reqparse.RequestParser()
    	parser.add_argument('nome', type=str)
    	parser.add_argument('cnpj', type=str)
    	parser.add_argument('razaoSocial', type=str)
    	parser.add_argument('nomeFantasia', type=str)
    	# print(parser.parse_args())
    	args = parser.parse_args()
    	e = Empresa(
    		nome = args['nome'],
			cnpj = args['cnpj'],
			razaoSocial = args['razaoSocial'],
			nomeFantasia = args['nomeFantasia'])
    	print('ARGS', args)
    	db.session.add(Empresa(**args))
    	db.session.commit()

    	return 'asdads'

    def post(self):
    	parser.add_argument('nome', type=str)
    	parser.add_argument('cnpj', type=str)
    	parser.add_argument('razaoSocial', type=str)
    	parser.add_argument('nomeFantasia', type=str)
    	

class Funcionario(Resource):
    def get(self):
    	# return db.
    	return 'adasd'


class Pedido(Resource):
	def get(self):
		return {'hello': 'Pedido'}

class Avaliacao(Resource):
    def get(self):
        return {'hello': 'Avaliacao'}

class Populate(Resource):
	def get(self):
		e = [Endereco(logradouro = 'logradouro',
				numero = 'numero',
				complemento = 'complemento',
				cep = 'cep',
				bairro = 'bairro',
				cidade = 'cidade'), ]
		c = [Contato(tipo = 'tipo',
				valor = 'valor')]
		db.session.add(Pessoa(nome = 'nome', sobrenome = 'sobrenome', cpf = 'cpf', enderecos =e, contatos = c, ))
		
		return 'asdadasd'
	def post(self):
		db.create_all()
		db.session.commit()



api.add_resource(Estabelecimento, '/estabelecimento')
api.add_resource(Funcionario, '/funcionario')
api.add_resource(Pedido, '/pedido')
api.add_resource(Avaliacao, '/avaliacao')
api.add_resource(Populate, '/populate')



app.run(debug = True)