from database import db


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True,
                   index=True, autoincrement=True)
    name = db.Column(db.String, unique=True, index=True)

    products = db.relationship("Product", back_populates="category")

    def to_json(self):
        return {"id": self.id, "name": self.name}
