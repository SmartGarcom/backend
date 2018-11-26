from flask_sqlalchemy import SQLAlchemy

'''
	Aqui coloquei os modelos do banco de dados
'''

db = SQLAlchemy()

Model, Column, String, Integer, Text, BigInteger = db.Model, db.Column, db.String, db.Integer, db.Text, db.BigInteger
Boolean = db.Boolean
Float  = db.Float
class Endereco(Model):
	__tablename__ = 'Endereco'
	logradouro = String(1000)
	numero = Integer(7)
	complemento = String(1000)
	cep = String(9)
	bairro = String(100)
	cidade = String(100)
	pessoa_fk = Pessoa()

class Contato(Model):
	__tablename__ = 'Contato'
	tipo = Integer(3)
	valor = String(1000)

class Pessoa(Model):
	__tablename__ = 'Pessoa'
	nome = String(100)
	sobrenome = String(250)
	cpf=BigInteger(11)

class Funcionario(Model):
	__tablename__ = 'Funcionario'
	cod = Integer(10)
	rg = String(13)

class CargoFuncionario(Model):
	__tablename__ = 'CargoFuncionario'
	nome = String(100)
	entregaPedido = Boolean
	montaPedido = Boolean

class Empresa(Model):
	__tablename__ = 'Empresa'
	nome = String(120)
	cnpj = String(15)
	razaoSocial = String(100)
	nomeFantasia = String(120)

class Item(Model):
	__tablename__ = 'Item'
	valor = Float(13)
	nome = String(123)
	codigo = String(100)

class PedidoItem(Model):
	__tablename__ = 'PedidoItem'
	quantidade = Float(12)
	valorUnitario = Float(12)
	desconto  = Float(12)
	valorTotalItem = Float(12)

class Pedido(Model):
	__tablename__ = 'Pedido'
	valorTotal  = Float(12)

class Pagamento(Model):
	__tablename__ = 'Pagamento'
	valor = Float(12)
	desconto = Float(12)

class FormaPagamento(Model):
	__tablename__ = 'FormaPagamento'
	nome = String(120)