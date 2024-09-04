from flask import Blueprint, request, jsonify
from app import db
from app.models.order import Order
from app.models.product import Product

order_bp = Blueprint('order', __name__)

@order_bp.route('/orders', methods=['POST'])
def place_order():
    data = request.json
    new_order = Order(order_date=data['order_date'], customer_id=data['customer_id'])
    db.session.add(new_order)
    for product_id in data['product_ids']:
        product = Product.query.get_or_404(product_id)
        new_order.products.append(product)
    db.session.commit()
    return jsonify({'id': new_order.id}), 201

@order_bp.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    products = [{'id': p.id, 'name': p.name, 'price': p.price} for p in order.products]
    return jsonify({
        'id': order.id,
        'order_date': order.order_date,
        'customer_id': order.customer_id,
        'products': products
    })
