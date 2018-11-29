from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_restful import Api

DB_URL = 'sqlite:///sqlite.sql'
# DB_URL = 'postgres://kiyvntduclansh:d74c329141605a04226d9b98186504a598d62be508c9a78ee4b7c34591e18fe4@ec2-54-227-249-201.compute-1.amazonaws.com:5432/ddr8j5sopft0ed' 
class Singleton(type):
   _instances = {}
   def __call__(cls, *args, **kwargs):
       if cls not in cls._instances:
           cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
       return cls._instances[cls]
       

class Factory(metaclass = Singleton):
	db, api, app = None, None, None

	def create_db(self):
		self.app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

		self.db = SQLAlchemy(self.app)
		self.db.create_all()
		self.db.session.commit()


	def create_api(self):
		self.api = Api(self.app)

	def create_app(self):
		self.app = Flask(__name__)
