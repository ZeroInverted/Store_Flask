from flask import Flask
from flask_cors import CORS
from routes.category_routes import category_blueprint
from routes.product_routes import product_blueprint
from database import db
from sqlalchemy import inspect

store = Flask(__name__)
CORS(store, resources={
    r"/categories/*": {
        "origins": "*"
    },
    r"/products/*": {
        "origins": "*"
    }
})

store.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
store.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


if __name__ == "__main__":
    with store.app_context():
        db.init_app(store)
        inspector = inspect(db.engine)
        if not inspector.has_table('categories'):
            db.create_all()
    store.register_blueprint(product_blueprint, url_prefix="/products")
    store.register_blueprint(category_blueprint, url_prefix="/categories")
    store.run()
