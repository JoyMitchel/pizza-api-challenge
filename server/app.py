from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from .config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

    db.init_app(app)
    migrate.init_app(app, db)

    from .controllers.restaurant_controller import restaurant_bp
    from .controllers.pizza_controller import pizza_bp
    from .controllers.restaurant_pizza_controller import restaurant_pizza_bp


    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)

    return app