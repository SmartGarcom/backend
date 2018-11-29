from flask_sqlalchemy import SQLAlchemy
from factory import Factory
'''
	Aqui coloquei os modelos do banco de dados
'''
db = SQLAlchemy()


Model, Column, String, Integer, Text, BigInteger = db.Model, db.Column, db.String, db.Integer, db.Text, db.BigInteger
Boolean = db.Boolean
Float  = db.Float
FK = db.ForeignKey
class Endereco(Model):
	__tablename__ = 'Endereco'
	id = Column(Integer, primary_key = True)
	logradouro = Column(String(1000), nullable = False)
	numero = Column(Integer, nullable = False)
	complemento = Column(String(1000), nullable = False)
	cep = Column(String(9), nullable = False)
	bairro = Column(String(100), nullable = False)
	cidade = Column(String(100), nullable = False)
	pessoa_fk = Column(Integer, FK('Pessoa.id'), nullable = False)

class Contato(Model):
	__tablename__ = 'Contato'
	id = Column(Integer, primary_key = True)
	tipo = Column(Integer, nullable = False)
	valor = Column(String(1000), nullable = False)
	pessoa_fk = Column(Integer, FK('Pessoa.id'), nullable = False)

class Pessoa(Model):
	__tablename__ = 'Pessoa'
	id = Column(Integer, primary_key = True)
	nome = Column(String(100), nullable = False)
	sobrenome = Column(String(250), nullable = False)
	cpf=Column(BigInteger, nullable = False)
	enderecos = db.relationship('Endereco')
	contatos = db.relationship('Contato', backref='pessoa', lazy = True)

class Funcionario(Model):
	__tablename__ = 'Funcionario'
	id = Column(Integer, primary_key = True)
	cod = Column(Integer, nullable = False)
	rg = Column(String(13), nullable = False)
	pessoa_fk = Column(Integer, FK('Pessoa.id'), nullable = False)
	empresa_fk = Column(Integer, FK('Empresa.id'), nullable = False)
	
	funcionario_fk = Column(Integer, FK('CargoFuncionario.id'), nullable = False)

class CargoFuncionario(Model):
	__tablename__ = "CargoFuncionario"
	id = Column(Integer, primary_key = True)
	nome = Column(String(30), nullable = False)
	entregaPedido = Column(Boolean, nullable = False)
	montaPedido = Column(Boolean, nullable = False)

	funcionario_fk = Column(Integer, FK('Funcionario.id'), nullable = False)
	
class Garcom(Model):
	__tablename__ = 'Garcom'
	id = Column(Integer, primary_key = True)
	funcionario_fk = Column(Integer, FK('Funcionario.id'), nullable = False)
	pedidoItens = db.relationship('PedidoItem', backref='garcom', lazy = True)

class Chef(Model):
	__tablename__ = 'Chef'
	id = Column(Integer, primary_key = True)
	funcionario_fk = Column(Integer, FK('Chef.id'), nullable = False)
	pedidoItens = db.relationship('PedidoItem', backref='chef', lazy = True)

class Gerente(Model):
	__tablename__ = 'Gerente'
	id = Column(Integer, primary_key = True)
	funcionario_fk = Column(Integer, FK('Gerente.id'), nullable = False)

class Empresa(Model):
	__tablename__ = 'Empresa'
	id = Column(Integer, primary_key = True)
	nome = Column(String(120), nullable = False)
	cnpj = Column(String(15), nullable = False)
	razaoSocial = Column(String(100), nullable = False)
	nomeFantasia = Column(String(120), nullable = False)
	funcionarios = db.relationship('Funcionario', backref='empresa', lazy = True)

class Item(Model):
	__tablename__ = 'Item'
	id = Column(Integer, primary_key = True)
	valor = Column(Float, nullable = False)
	nome = Column(String(123), nullable = False)
	codigo = Column(String(100), nullable = False)
	pedidoItens = db.relationship('PedidoItem', backref='item', lazy = True)


class PedidoItem(Model):
	__tablename__ = 'PedidoItem'
	id = Column(Integer, primary_key = True)
	quantidade = Column(Float, nullable = False)
	valorUnitario = Column(Float, nullable = False)
	desconto  = Column(Float, nullable = False)
	valorTotalItem = Column(Float, nullable = False)

	garcom_fk = Column(Integer, FK('Garcom.id'))
	chef_fk = Column(Integer, FK('Chef.id'))

	item_fk = Column(Integer, FK('Item.id'))
	pedido_fk = Column(Integer, FK('Pedido.id'))

class Pedido(Model):
	__tablename__ = 'Pedido'
	id = Column(Integer, primary_key = True)
	valorTotal  = Column(Float, nullable = False)
	pedidoItens = db.relationship('PedidoItem', backref='pedido', lazy = True)


class Pagamento(Model):
	__tablename__ = 'Pagamento'
	id = Column(Integer, primary_key = True)
	valor = Column(Float, nullable = False)
	desconto = Column(Float, nullable = False)
	pedido_fk = Column(Integer, FK('Pedido.id'))
	formas_pagamento = db.relationship('FormaPagamento', backref='pagemento', lazy = True)



class FormaPagamento(Model):
	__tablename__ = 'FormaPagamento'
	id = Column(Integer, primary_key = True)
	nome = String(120)
	pagamento_fk = Column(Integer, FK('Pagamento.id'))
