from models.category_model import Category
from database import db


def get_all_categories():
    return [Category.to_json(category) for category in Category.query.all()]


def add_category(category_name):
    new_category = Category(name=category_name)
    db.session.add(new_category)
    db.session.commit()
    db.session.refresh(new_category)
    return Category.to_json(new_category)
