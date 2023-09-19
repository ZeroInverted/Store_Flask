from database import db
import json


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, unique=True, index=True)

    products = db.relationship("Product", back_populates="category")

    def get_all_categories():
        return [Category.to_json(category) for category in Category.query.all()]

    def add_category(category_name):
        new_category = Category(name=category_name)
        db.session.add(new_category)
        db.session.commit()
        db.session.refresh(new_category)
        return Category.to_json(new_category)

    def to_json(self):
        return {"name": self.name}
