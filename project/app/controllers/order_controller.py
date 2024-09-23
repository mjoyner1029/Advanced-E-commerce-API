from flask import Blueprint, request, jsonify
from app.models.order import Order
from app.models.product import Product
from app.models.customer import db
from flask_jwt_extended import jwt_required

order_bp = Blueprint('order', __name__)

@order_bp.route('/orders', methods=['POST'])
@jwt_required()
def place_order():
    data = request.json
    new_order = Order(order_date=data['order_date'], customer_id=data['customer_id'])
    for product_id in data['product_ids']:
        product = Product.query.get(product_id)
        if product:
            new_order.products.append(product)
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'id': new_order.id}), 201

@order_bp.route('/orders/<int:order_id>', methods=['GET'])
@jwt_required()
def retrieve_order(order_id):
    order = Order.query.get_or_404(order_id)
    return jsonify({
        'id': order.id,
        'order_date': order.order_date,
        'customer_id': order.customer_id,
        'products': [product.id for product in order.products]
    })
