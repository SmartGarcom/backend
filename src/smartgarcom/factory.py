from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_restful import Api


DB_URL = '' # TODO: Colocar aqui o URL do DB

def create_db(app):
	app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
	return SQLAlchemy(app)

def create_api(app):
	return Api(app)

def create_app():
	return Flask(__name__)
