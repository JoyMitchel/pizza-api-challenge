from flask import Blueprint, jsonify, request
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza
from server.app import db

restaurant_bp = Blueprint('restaurant_bp', __name__, url_prefix='/restaurants')

@restaurant_bp.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{"id": r.id, "name": r.name, "address": r.address} for r in restaurants])