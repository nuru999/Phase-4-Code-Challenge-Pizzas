# import unittest,json
from flask import Flask
# from api import app,api  # Replace 'your_app_module' with the actual module name
# Import the necessary models
from api.models import db, Restaurant ,RestaurantPizza
from sqlalchemy.orm import class_mapper


class TestRestaurantsRoute():
  
    def test_restaurant_model_has_correct_columns(sefl):
        '''the Restaurant model has the correct attribut/columns'''
        # set a class instance
        restaurant = Restaurant()
        # get the class mapper
        mapper = class_mapper(restaurant.__class__)
        # loop thru the mapper and get a list of the columns
        columns = [column.key for column in mapper.columns]
        #the columns we need to have and are expecting
        expected_cols = ['name','id','address']
        assert set(columns) == set(expected_cols)

    def test_restaurant_model_has_validates_decorator(sefl):
        '''the Restaurant model has a name validator'''
        assert hasattr(Restaurant, 'name_validation')



      
    def test_restaurantPizza_model_has_correct_columns(sefl):
        '''the Pizza model has the correct attribut/columns'''
        # set a class instance
        restaurant_pizza = RestaurantPizza()
        # get the class mapper
        mapper = class_mapper(restaurant_pizza.__class__)
        # loop thru the mapper and get a list of the columns
        columns = [column.key for column in mapper.columns]
        #the columns we need to have and are expecting
        expected_cols = ['id','price','created_at','updated_at','pizza_id','restaurant_id',]
        assert set(columns) == set(expected_cols)

    def test_restaurantPizza_model_has_validates_decorator(sefl):
        '''the Restaurant model has a name validator'''
        assert hasattr(RestaurantPizza, 'price_validation')











#     def test_get_restaurants(self):
#         # Test the GET request to retrieve all restaurants
#         response = self.client.get('/restaurants')
        
#         # Check if the response status code is 200 (OK)
#         self.assertEqual(response.status_code, 200)
        
#         # Check if the response contains the expected data
#         expected_data = [
#             {"id": 1, "name": "Restaurant 1", "address": "Address 1"},
#             {"id": 2, "name": "Restaurant 2", "address": "Address 2"},
#         ]
#         self.assertEqual(response.get_json(), expected_data)

#     def test_get_restaurant_by_id(self):
#         # Test the GET request to retrieve a specific restaurant by ID
#         response = self.client.get('/restaurants/1')
        
#         # Check if the response status code is 200 (OK)
#         self.assertEqual(response.status_code, 200)
        
#         # Check if the response contains the expected data for Restaurant 1
#         expected_data = {"id": 1, "name": "Restaurant 1", "address": "Address 1"}
#         self.assertEqual(response.get_json(), expected_data)

#     def test_get_nonexistent_restaurant_by_id(self):
#         # Test the GET request for a non-existent restaurant by ID
#         response = self.client.get('/restaurants/100')  # Assuming there is no restaurant with ID 100
        
#         # Check if the response status code is 404 (Not Found)
#         self.assertEqual(response.status_code, 404)
        
#         # Check if the response contains an error message
#         expected_data = {"error": "Restaurant not found"}
#         self.assertEqual(response.get_json(), expected_data)

# if __name__ == '__main__':
#     unittest.main()
