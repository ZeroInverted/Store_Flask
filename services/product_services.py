from models.product_model import Product
from database import db


def get_all_products() -> list[dict]:
    return [Product.to_json(product) for product in Product.query.all()]


def add_product(p_name, p_price, p_quantity, p_img_url, p_category_id):
    new_product = Product(name=p_name, price=p_price, quantity=p_quantity,
                          img_url=p_img_url, category_id=p_category_id)
    db.session.add(new_product)
    db.session.commit()
    db.session.refresh(new_product)
    return Product.to_json(new_product)


def get_product_by_id(id) -> dict:
    return Product.to_json(Product.query.filter(Product.id == id).first())


def update_product(id, p_name, p_price, p_quantity, p_img_url, p_category_id) -> dict:
    product_to_update = Product.query.filter(Product.id == id).first()
    product_to_update.name = p_name
    product_to_update.price = p_price
    product_to_update.quantity = p_quantity
    product_to_update.img_url = p_img_url
    product_to_update.category_id = p_category_id
    db.session.commit()
    return Product.to_json(product_to_update)


def get_products_by_cat_id(cat_id) -> list[dict]:
    return [Product.to_json(product) for product in Product.query.filter(Product.category_id == cat_id)]
