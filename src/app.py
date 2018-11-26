from flask import Flask, render_template, request, url_for, redirect, Response, current_app
from database import db

app = Flask(__name__)
app.secret_key = os.urandom(64)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    db.init_app(app)
    # db.drop_all()
    db.create_all()

@app.route(f'{API_PREFIX}/')
def index():
	return "O AMBIENTE ESTA CONFIGURADO"