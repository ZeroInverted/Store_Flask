from flask import Blueprint, request, jsonify
from schemas.product_schema import ProductInput
from services.product_services import get_all_products, get_product_by_id, get_products_by_cat_id, add_product, update_product

product_blueprint = Blueprint("product", __name__)


@product_blueprint.route("/", methods=["GET", "POST"])
def category_operations():
    if request.method == "GET":
        return jsonify(get_all_products())
    elif request.method == "POST":
        data = request.json
        new_product = ProductInput(**data)
        return jsonify(add_product(p_name=new_product.name,
                                   p_price=new_product.price,
                                   p_quantity=new_product.quantity,
                                   p_img_url=new_product.img_url,
                                   p_category_id=new_product.category_id))
