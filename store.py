from flask import Flask

store = Flask(__name__)

store.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
store.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
