from flask import Blueprint, request, jsonify
from app.models.product import Product, db
from flask_jwt_extended import jwt_required

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['POST'])
@jwt_required()
def create_product():
    data = request.json
    new_product = Product(name=data['name'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'id': new_product.id}), 201

@product_bp.route('/products/<int:product_id>', methods=['GET'])
@jwt_required()
def read_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price})

@product_bp.route('/products/<int:product_id>', methods=['PUT'])
@jwt_required()
def update_product(product_id):
    data = request.json
    product = Product.query.get_or_404(product_id)
    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    db.session.commit()
    return jsonify({'message': 'Product updated'}), 200

@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted'}), 204

@product_bp.route('/products', methods=['GET'])
@jwt_required()
def list_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price} for p in products]), 200
