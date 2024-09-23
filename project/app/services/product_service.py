from app.models.product import Product
from app.utils.app import db

def create_product(name, price):
    new_product = Product(name=name, price=price)
    db.session.add(new_product)
    db.session.commit()
    return new_product

def get_product(product_id):
    return Product.query.get(product_id)

def update_product(product_id, name=None, price=None):
    product = get_product(product_id)
    if name:
        product.name = name
    if price is not None:
        product.price = price
    db.session.commit()
    return product

def delete_product(product_id):
    product = get_product(product_id)
    db.session.delete(product)
    db.session.commit()
