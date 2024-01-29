from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Pizza, RestaurantPizza, Restaurant

app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build'
)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h2>This is the home page</h2>'

# GET /restaurants endpoint:
@app.route("/restaurants", methods=['GET'])
def restaurant():
    if request.method == "GET":
        restaurants = []
        for restaurant in Restaurant.query.all():
            res_dict = {
                'id':restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address 
            }
            restaurants.append(res_dict)
  
        return make_response(jsonify(restaurants), 200)

@app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def restaurant_by_id(id):
    restaurant = Restaurant.query.filter(Restaurant.id ==id).first()

    # If the `Restaurant` does not exist, return the JSON data below,
    if not restaurant:
        return make_response(jsonify({"error": "Restaurant not found"}))
    
    if request.method == "GET":
        restaurant_dict = {
                'id':restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address,
                "pizzas": [
                    {
                        "id": restaurant_pizza.pizza.id,
                        "name": restaurant_pizza.pizza.name,
                        "ingredients": restaurant_pizza.pizza.ingredients
                    }
                    for restaurant_pizza in restaurant.restaurant_pizzas 
                ]
            }
            

        return make_response(restaurant_dict, 200)
    
    elif request.method == "DELETE":
        try:
            # Delete associated RestaurantPizza first
            for restaurant_pizza in restaurant.restaurant_pizzas:
                db.session.delete(restaurant_pizza)

            # delete the Restaurant data
            db.session.delete(restaurant)
            db.session.commit()

            response_body = {
                "success": True,
                "message": "Restaurant deleted successfully."
            }

            return make_response(jsonify(response_body), 200)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)

# Get a single data
@app.route("/pizzas", methods=['GET'])
def pizzas():
    if request.method == 'GET':
        
        get_pizzas = Pizza.query.all()
        pizzas_dict = [
            {
                'id':pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            }
            for pizza in get_pizzas
        ]

        return jsonify(pizzas_dict)
        

@app.route('/pizzas/<int:id>', methods=['GET'])
def pizza_by_id(id):
    pizza = Pizza.query.filter(Pizza.id ==id).first()

    if request.method == "GET":
        pizzas_dict = {
                'id':pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            }
            

        return make_response(pizzas_dict, 200)

# Get restaurant_pizza
@app.route("/restaurant_pizzas", methods=["GET", "POST"])
def restaurant_pizza():
    if request.method == "GET":
        get_pizzas = Pizza.query.all()
        pizzas_dict = [
            {
                'id':pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            }
            for pizza in get_pizzas
        ]

        return jsonify(pizzas_dict)

    elif request.method == "POST":
        try:
            # Extract data from the response request body 
            data = request.json
            price = data.get("price")
            pizza_id = data.get("pizza_id")
            restaurant_id = data.get("restaurant_id")

            # Validate the input data
            if price is None or pizza_id is None or restaurant_id is None:
                return make_response(jsonify({"error": "Incomplete data"}), 400)

            # Check if the Pizza and Restaurant exist
            pizza = Pizza.query.get(pizza_id)
            restaurant = Restaurant.query.get(restaurant_id)

            if not pizza or not restaurant:
                return make_response(jsonify({"error": "Pizza or Restaurant not found"}), 404)

            # Create a new Restaurant_Pizza instance
            new_restaurant_pizza = RestaurantPizza(
                price=price,
                pizza_id=pizza_id,
                restaurant_id=restaurant_id
            )

            # Add the new RestaurantPizza to the database
            db.session.add(new_restaurant_pizza)
            db.session.commit()

            # Return a success response
            response_body = {
                "success": True,
                "message": "RestaurantPizza created successfully."
            }

            return make_response(jsonify(response_body), 201)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)

if __name__ == '__main__':
    app.run(debug=True)