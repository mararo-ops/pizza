from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# Route to get all restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = []

    for restaurant in restaurants:
        restaurant_data = {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        }

        restaurant_list.append(restaurant_data)

    return jsonify(restaurant_list), 200    

# Route to get a specific restaurant by ID
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)

    if restaurant is None:
        return jsonify({"error": "Restaurant not found"}), 404

    # Retrives associated pizzas
    pizzas = []
    for restaurant_pizza in restaurant.restaurant_pizzas:
        pizza = restaurant_pizza.pizza
        pizza_data = {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }
        pizzas.append(pizza_data)

    restaurant_data = {
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": pizzas
    }

    return jsonify(restaurant_data)
