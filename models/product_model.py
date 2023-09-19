from database import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, index=True)
    price = db.Coluimn(db.Float)
    quantity = db.Column(db.Integer)
    img_url = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    category = db.relationship("Category", back_populates="products")
