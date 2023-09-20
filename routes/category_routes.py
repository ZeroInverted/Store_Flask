from flask import Blueprint, request, jsonify
from schemas.category_schema import CategoryInput
from services.category_services import get_all_categories, add_category

category_blueprint = Blueprint("category", __name__)


@category_blueprint.route("/", methods=["GET", "POST"])
def category_operations():
    if request.method == "GET":
        return jsonify(get_all_categories())
    elif request.method == "POST":
        data = request.json
        new_category = CategoryInput(**data)
        return jsonify(add_category(new_category.name))
