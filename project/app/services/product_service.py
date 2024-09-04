from app.models.product import Product

def get_product_by_id(product_id):
    return Product.query.get(product_id)
