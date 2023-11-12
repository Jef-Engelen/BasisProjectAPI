from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

# Item model klasse
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# Aanmaken tabellen in database
db.create_all()

# Parser voor PUT en POST requests
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)

class ItemListResource(Resource):
    #GET endpoint
    def get(self):
        items = Item.query.all()
        items_list = [{'id': item.id, 'name': item.name} for item in items]
        return jsonify({'items': items_list})

    #POST endpoint
    def post(self):
        args = parser.parse_args()
        new_item = Item(name=args['name'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'item': {'id': new_item.id, 'name': new_item.name}}), 201

class ItemResource(Resource):

    #GET endpoint
    def get(self, item_id):
        item = Item.query.get(item_id)
        if item:
            return jsonify({'item': {'id': item.id, 'name': item.name}})
        else:
            return jsonify({'message': 'Item not found'}), 404

    #DELETE endpoint
    def delete(self, item_id):
        item = Item.query.get(item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return jsonify({'message': 'Item deleted'}), 200
        else:
            return jsonify({'message': 'Item not found'}), 404

    #PUT endpoint
    def put(self, item_id):
        args = parser.parse_args()
        item = Item.query.get(item_id)
        if item:
            item.name = args['name']
            db.session.commit()
            return jsonify({'item': {'id': item.id, 'name': item.name}})
        else:
            return jsonify({'message': 'Item not found'}), 404

api.add_resource(ItemListResource, '/api/items')
api.add_resource(ItemResource, '/api/items/<int:item_id>')

if __name__ == '__main__':
    app.run(debug=True)
