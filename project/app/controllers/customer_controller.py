from flask import Blueprint, request, jsonify
from app.models.customer import Customer, CustomerAccount, db
from flask_jwt_extended import jwt_required

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/customers', methods=['POST'])
@jwt_required()
def create_customer():
    data = request.json
    new_customer = Customer(name=data['name'], email=data['email'], phone=data.get('phone'))
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({'id': new_customer.id}), 201

@customer_bp.route('/customers/<int:customer_id>', methods=['GET'])
@jwt_required()
def read_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return jsonify({'id': customer.id, 'name': customer.name, 'email': customer.email, 'phone': customer.phone})

@customer_bp.route('/customers/<int:customer_id>', methods=['PUT'])
@jwt_required()
def update_customer(customer_id):
    data = request.json
    customer = Customer.query.get_or_404(customer_id)
    customer.name = data.get('name', customer.name)
    customer.email = data.get('email', customer.email)
    customer.phone = data.get('phone', customer.phone)
    db.session.commit()
    return jsonify({'message': 'Customer updated'}), 200

@customer_bp.route('/customers/<int:customer_id>', methods=['DELETE'])
@jwt_required()
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({'message': 'Customer deleted'}), 204
