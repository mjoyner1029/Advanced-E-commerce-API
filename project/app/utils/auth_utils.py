from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

def create_token(identity, expires_delta=None):
    return create_access_token(identity=identity, expires_delta=expires_delta)

def jwt_required_admin(fn):
    return jwt_required(fn)
