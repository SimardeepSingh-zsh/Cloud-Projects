from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify(products=[product.serialize() for product in products])

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product.serialize())

@app.route('/products', methods=['POST'])
def add_product():
    # Add product to the database
    pass

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    # Update product in the database
    pass

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    # Delete product from the database
    pass