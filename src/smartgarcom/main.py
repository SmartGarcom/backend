from factory import create_db, create_app, create_api
from core.endpoints import HelloWorld


app = create_app()
api = create_api(app)
db = create_db(app)

api.add_resource(HelloWorld, '/')

app.run(debug = True)