from flask_sqlalchemy import SQLAlchemy

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
	logradouro = String(1000)
	numero = Integer(7)
	complemento = String(1000)
	cep = String(9)
	bairro = String(100)
	cidade = String(100)
	pessoa_fk = Column(Integer, FK('pessoa.id'), nullable = False)

class Contato(Model):
	__tablename__ = 'Contato'
	tipo = Integer(3)
	valor = String(1000)
	pessoa_fk = Column(Integer, FK('pessoa.id'), nullable = False)

class Pessoa(Model):
	__tablename__ = 'Pessoa'
	nome = String(100)
	sobrenome = String(250)
	cpf=BigInteger(11)
	enderecos = db.relationship('Endereco', backref='pessoa', lazy = True)
	contatos = db.relationship('Contato', backref='pessoa', lazy = True)

class Funcionario(Model):
	__tablename__ = 'Funcionario'
	cod = Integer(10)
	rg = String(13)
	pessoa_fk = Column(Integer, FK('pessoa.id'), nullable = False)
	empresa_fk = Column(Integer, FK('empresa.id'), nullable = False)
	
	funcionario_fk = Column(Integer, FK('cargofuncionario.id'), nullable = False)

class CargoFuncionario(Model):
	__tablename__ = "CargoFuncionario"
	nome = Column(String('30'), nullable = False)
	entregaPedido = Column(Boolean, nullable = False)
	montaPedido = Column(Boolean, nullable = False)

	funcionario_fk = Column(Integer, FK('funcionario.id'), nullable = False)
	
class Garcom(Model):
	__tablename__ = 'Garcom'
	funcionario_fk = Column(Integer, FK('funcionario.id'), nullable = False)
	pedidoItens = db.relationship('PedidoItem', backref='garcom', lazy = True)

class Chef(Model):
	__tablename__ = 'Garcom'
	funcionario_fk = Column(Integer, FK('chef.id'), nullable = False)
	pedidoItens = db.relationship('PedidoItem', backref='chef', lazy = True)

class Gerente(Model):
	__tablename__ = 'Garcom'
	funcionario_fk = Column(Integer, FK('gerente.id'), nullable = False)

class Empresa(Model):
	__tablename__ = 'Empresa'
	nome = String(120)
	cnpj = String(15)
	razaoSocial = String(100)
	nomeFantasia = String(120)
	funcionarios = db.relationship('Funcionario', backref='empresa', lazy = True)

class Item(Model):
	__tablename__ = 'Item'
	valor = Float(13)
	nome = String(123)
	codigo = String(100)
	pedidoItens = db.relationship('PedidoItem', backref='item', lazy = True)


class PedidoItem(Model):
	__tablename__ = 'PedidoItem'
	quantidade = Float(12)
	valorUnitario = Float(12)
	desconto  = Float(12)
	valorTotalItem = Float(12)

	garcom_fk = Column(Integer, FK('garcom.id'))
	chef_fk = Column(Integer, FK('chef.id'))

	item_fk = Column(Integer, FK('item.id'))
	pedido_fk = Column(Integer, FK('pedido.id'))

class Pedido(Model):
	__tablename__ = 'Pedido'
	valorTotal  = Float(12)
	pedidoItens = db.relationship('PedidoItem', backref='pedido', lazy = True)


class Pagamento(Model):
	__tablename__ = 'Pagamento'
	valor = Float(12)
	desconto = Float(12)
	pedido_fk = Column(Integer, FK('pedido.id'))
	formas_pagamento = db.relationship('FormaPagamento', backref='pagemento', lazy = True)



class FormaPagamento(Model):
	__tablename__ = 'FormaPagamento'
	nome = String(120)
	pagamento_fk = Column(Integer, FK('pagamento.id'))
