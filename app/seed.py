from faker import Faker
from random import randint, choice
from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

fake = Faker()

with app.app_context():
    # Clear existing data
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    # Seeding the restaurants
    restaurants = []
    for _ in range(20):
        restaurant = Restaurant(
            name=fake.company(),
            address=fake.address()
        )
        restaurants.append(restaurant)

    db.session.add_all(restaurants)
    db.session.commit()