from flask import Blueprint
from app.controllers.customer_controller import customer_bp
from app.controllers.order_controller import order_bp
from app.controllers.product_controller import product_bp

api_bp = Blueprint('api', __name__)
api_bp.register_blueprint(customer_bp, url_prefix='/api')
api_bp.register_blueprint(order_bp, url_prefix='/api')
api_bp.register_blueprint(product_bp, url_prefix='/api')
