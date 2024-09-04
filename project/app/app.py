from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_limiter import Limiter
from flask_jwt_extended import JWTManager
from config import Config

db = SQLAlchemy()
cache = Cache()
limiter = Limiter(key_func=lambda: 'global', default_limits=[Config.LIMITER_LIMIT])
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)
    jwt.init_app(app)

    from app.routes.api_routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
