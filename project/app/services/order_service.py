from app.models.order import Order
from app.models.product import Product
from app.utils.app import db

def place_order(order_date, customer_id, product_ids):
    new_order = Order(order_date=order_date, customer_id=customer_id)
    for product_id in product_ids:
        product = Product.query.get(product_id)
        if product:
            new_order.products.append(product)
    db.session.add(new_order)
    db.session.commit()
    return new_order

def get_order(order_id):
    return Order.query.get(order_id)
