import unittest,json
from flask import Flask
from api import app,api  # Replace 'your_app_module' with the actual module name
from api.models import db, Restaurant  # Import the necessary models

class TestRestaurantsRoute():
  
    
    def test_restaurants_route(self):
        '''does the resource exist  at "/restaurants".'''
        response = app.test_client().get('/restaurants')
        assert(response.status_code == 200)

    def test_restaurants_route_returns_json(self):
        '''provides a response content type of application/json at "/restaurants"'''
        response = app.test_client().get('/restaurants')
        assert response.content_type == 'application/json'

    def test_restaurant_route_returns_list_of_restaurant_objsects(self):
        '''restaurant route returns a list of restaurant objects'''
#         # Add some test data to the database
        with app.app_context():
            restaurant1 = Restaurant(name='Restaurant 1', address='Address 1')
            restaurant2 = Restaurant(name='Restaurant 2', address='Address 2')
            db.session.add_all([restaurant1,restaurant2])
            db.session.commit()
            response = app.test_client().get('/restaurants')
            data = json.loads(response.data.decode())
            assert(type(data)==list)


    def test_restaurant_by_id_route(self):
        '''has resource available at /restaurants/1'''
        response = app.test_client().get('/restaurants/1')
        assert(response.status_code ==200)

    def test_restaurant_by_id_route_returns_json(self):
        '''the route return a json object in the  response body'''
        response = app.test_client().get('/restaurants/1')
        assert response.content_type=='application/json'

    def test_restaurant_by_id_route_response_contains_pizza_list(self):
        '''    pizzas exists in the response and is a type of list'''
        response = app.test_client().get('/restaurants/1')
        data = json.loads(response.data.decode())
        assert "pizzas" in data and isinstance(data["pizzas"], list)
