from flask_restful import Resource,reqparse
from factory import Factory
from model import *
import inspect

fac = Factory()

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
    	fac.db.session.add(e)
    	fac.db.session.commit()

    	return 'asdads'

    def post(self):
    	parser.add_argument('nome', type=str)
    	parser.add_argument('cnpj', type=str)
    	parser.add_argument('razaoSocial', type=str)
    	parser.add_argument('nomeFantasia', type=str)
    	

class Funcionario(Resource):
    def get(self):
    	# return fac.db.
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
		fac.db.session.add(Pessoa(nome = 'nome', sobrenome = 'sobrenome', cpf = 'cpf', enderecos =e, contatos = c, ))
		
		return 'asdadasd'
	def post(self):
		fac.db.create_all()
		fac.db.session.commit()