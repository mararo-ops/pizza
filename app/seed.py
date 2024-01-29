from models import Pizza, Restaurant, RestaurantPizza
from app import db, app

pizzas = [
    {
        "name": "Margheritai", 
        "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
        "name": "Pepperoni", 
        "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    },
    {
        "name": "Vegetarian", 
        "ingredients": "Dough, Tomato Sauce, Cheese, Mushrooms, Bell Peppers, Onions"
    },
    {
        "name": "Hawaiian", 
        "ingredients": "Dough, Tomato Sauce, Cheese, Ham, Pineapple"
    },
    {
        "name": "Meat Lovers", 
        "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni, Sausage, Bacon"
    },
    {
        "name": "BBQ Chicken", 
        "ingredients": "Dough, BBQ Sauce, Cheese, Chicken, Red Onion, Cilantro"
    }
]

restaurants = [
    {
        "name": "Italiano Delight",
        "address": "123 Main St, City, Country"
    },
    {
        "name": "Pasta Paradise",
        "address": "456 Oak St, Town, Country"
    },
    {
        "name": "Mamma Mia Pizzeria",
        "address": "789 Pine St, Village, Country"
    },
    {
        "name": "Pizza Palace",
        "address": "101 Elm St, Hamlet, Country"
    },
    {
        "name": "Savory Slices",
        "address": "202 Maple St, Suburb, Country"
    },
    {
        "name": "Rustic Retreat",
        "address": "303 Cedar St, Countryside, Country"
    },
    {
        "name": "Mozzarella Haven",
        "address": "404 Birch St, Rural, Country"
    }
]

pizzaRestaurants = [
    {
        "price": 10,
        "pizza_id": 1,
        "restaurant_id": 1
    },
    {
        "price": 12,
        "pizza_id": 2,
        "restaurant_id": 2
    },
    {
        "price": 15,
        "pizza_id": 3,
        "restaurant_id": 3
    },
    {
        "price": 14,
        "pizza_id": 4,
        "restaurant_id": 4
    },
]

with app.app_context():
 
    db.session.add_all([Pizza(**pizza) for pizza in pizzas])
    db.session.commit()

    db.session.add_all([Restaurant(**restaurant) for restaurant in restaurants])
    db.session.commit()

    db.session.add_all([RestaurantPizza(**rp) for rp in pizzaRestaurants])
    db.session.commit()
