from flask import Flask,render_template
from flask_restful import Api
from flask_jwt import JWT

from resources.user import UserRegister
from security import authenticated, identity
from resources.item import Item,ListItem
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "key_secret"
api = Api(app)

jwt = JWT(app, authenticated, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ListItem, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)