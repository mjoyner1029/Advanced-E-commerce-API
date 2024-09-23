from flask_jwt_extended import create_access_token
from app.models.customer_account import CustomerAccount

def generate_jwt(user):
    return create_access_token(identity={'username': user.username}, fresh=True)
