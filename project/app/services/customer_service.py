from app.models.customer import Customer, CustomerAccount
from app.utils.app import db

def create_customer(name, email, phone):
    new_customer = Customer(name=name, email=email, phone=phone)
    db.session.add(new_customer)
    db.session.commit()
    return new_customer

def get_customer(customer_id):
    return Customer.query.get(customer_id)

def update_customer(customer_id, name=None, email=None, phone=None):
    customer = get_customer(customer_id)
    if name:
        customer.name = name
    if email:
        customer.email = email
    if phone:
        customer.phone = phone
    db.session.commit()
    return customer

def delete_customer(customer_id):
    customer = get_customer(customer_id)
    db.session.delete(customer)
    db.session.commit()
