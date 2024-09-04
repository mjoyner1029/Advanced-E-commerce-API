from app.models.order import Order

def get_order_by_id(order_id):
    return Order.query.get(order_id)
