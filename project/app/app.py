from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.routes.api_routes import api_bp
from app.utils.config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(api_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
