from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData,UniqueConstraint
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    serialize_rules = ('-rest_pizza_association.restaurants','pizzas',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    UniqueConstraint('name', name='unique_rest_name')

    # relationship
    rest_pizza_association = db.relationship('RestaurantPizza', back_populates ='restaurant',cascade='all, delete-orphan')
    pizzas = association_proxy('rest_pizza_association', 'pizza')


    # ---------------------------------------validations
    @validates('name')
    def name_validation(self, key, name):
        if len(name)>=50:
            raise ValueError('Name must be less than 50 characters')
        return name
    


    def __repr__(self):
        return f'(id: {self.id}, name: {self.name}. address: {self.address})'


class RestaurantPizza(db.Model,SerializerMixin):
    __tablename__='restaurant_pizzas'

    serialize_rules =('-pizza.rest_pizza_association', '-restaurant.rest_pizza_association',)

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
  
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    pizza_id = db.Column('pizza_id',db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column('restaurant_id',db.Integer, db.ForeignKey('restaurants.id'))
    

    pizza = db.relationship('Pizza',back_populates='rest_pizza_association')
    restaurant = db.relationship('Restaurant',back_populates='rest_pizza_association')



    # ------------------------------------------validations
    @validates('price')
    def price_validation(self, key, price):
        if int(price) > 30:
            raise ValueError('Price must be between KSH 1 and KSH 30')
        
        return '$ ' + str(price)
    
    


    

    def __repr__(self):
        return f'(id: {self.id}, name: {self.price}, pizza_id: {self.pizza_id}, restaurant_id: {self.restaurant_id})'



class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'


    serialize_rules = ('-rest_pizza_association',)


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # relationship
    rest_pizza_association = db.relationship('RestaurantPizza', back_populates ='pizza')
    restaurants = association_proxy('rest_pizza_association', 'restaurant')
    

    def get_price(self):
        return self.rest_pizza_association[0].price

    def __repr__(self):
        return f'(id: {self.id}, name: {self.name}, pizza_id: {self.ingredients}, restaurant_id: {self.created_at})'


