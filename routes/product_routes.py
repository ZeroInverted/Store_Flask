from flask import Blueprint, abort, request, jsonify
from schemas.product_schema import ProductInput
from services.product_services import get_all_products, get_product_by_id, get_products_by_cat_id, add_product, update_product

product_blueprint = Blueprint("product", __name__)


@product_blueprint.route("/", methods=["GET", "POST"])
def product_general_operations():
    if request.method == "GET":
        search_by_category = request.args.get("categoryID")
        if search_by_category:
            return jsonify(get_products_by_cat_id(search_by_category))
        else:
            return jsonify(get_all_products())
    elif request.method == "POST":
        data = request.json
        new_product = ProductInput(**data)
        return jsonify(add_product(p_name=new_product.name,
                                   p_price=new_product.price,
                                   p_quantity=new_product.quantity,
                                   p_img_url=new_product.img_url,
                                   p_category_id=new_product.category_id))


@product_blueprint.route("/<int:id>", methods=["GET", "PUT"])
def product_specific_operations(id: int):
    if request.method == "GET":
        try:
            product = get_product_by_id(id)
            return jsonify(product)
        except:
            abort(404)
    elif request.method == "PUT":
        data = request.json
        new_product = ProductInput(**data)
        return jsonify(update_product(id=id, p_name=new_product.name,
                                      p_price=new_product.price,
                                      p_quantity=new_product.quantity,
                                      p_img_url=new_product.img_url,
                                      p_category_id=new_product.category_id))
# Return JSON instead of HTTP errors.


@product_blueprint.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Product not found"
    }), 404


@product_blueprint.errorhandler(500)
def server_error(error):
    return jsonify({
        "error": "Internal server error"
    }), 500
