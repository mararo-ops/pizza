from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255))

    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant')
    
    def __repr__(self):
        return f'<Restaurant {self.id}: {self.name}'

    def validate(self):
        errors = {}

        if not self.name:
            errors['name'] = 'Name is required'

        if len(self.name) > 50:
            errors['name'] = 'Name must be less than 50 characters long'

        return errors
