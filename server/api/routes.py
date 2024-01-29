from api import make_response,jsonify,app
from flask import request
# from flask_restful import Resource
from flask_restx import Api,Resource,Namespace
from api.models import Restaurant,RestaurantPizza,Pizza,db,SerializerMixin


app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] =False


api = Api()
api.init_app(app)
RX=Namespace('api')
api.add_namespace(RX)

@RX.route('/')
class Restaurants(Resource):
    def home(self):
        restaurants = Restaurant.query.all()

        restaurant_dict_list =[]
        for restaurant in restaurants:
            restuarant_dict = {
                "id":restaurant.id,
                "name":restaurant.name,
                "address":restaurant.address
            }
            restaurant_dict_list.append(restuarant_dict)
        

        return make_response(restaurant_dict_list,200)

    def get(self):
        restaurants = Restaurant.query.all()

        restaurant_dict_list =[]
        for restaurant in restaurants:
            restuarant_dict = {
                "id":restaurant.id,
                "name":restaurant.name,
                "address":restaurant.address
            }
            restaurant_dict_list.append(restuarant_dict)
        
        
        return make_response(restaurant_dict_list,200)

# api.add_resource(Restaurants, '/')





@RX.route('/restaurants/<int:id>')
class Restaurants_by_ID(Resource,SerializerMixin):
    def get(self,id):
        restaurant = Restaurant.query.filter_by(id=id).first()

        if restaurant:      
            restuarant_dict = restaurant.to_dict()        
            return make_response(restuarant_dict,200)
        else:
            response = { "error": "Restaurant not found" }
            return make_response(response,404)
        


    def delete(self,id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()

            response = {
                "delete-successful":True,
                "message": "restaurant deleted"
            }
            return make_response(jsonify(response),204)
        
        else:
            response = { "error": "restaurant you are trying to delete DOES NOT EXIST" }
            return make_response(response,404)
            






@RX.route('/pizzas')
class Pizzas(Resource):
        def get(sefl):
            pizzas = Pizza.query.all()

            pizza_dict_list =[]
            for pizza in pizzas:
                pizza_dict = pizza.to_dict()
                # get the price of the pizza
                pizza_price = pizza.get_price()
                pizza_dict.update({'price': pizza_price})

                pizza_dict_list.append(pizza_dict)


            # response_data = {'pizzas':pizza_dict_list}            
            return make_response(pizza_dict_list,200)



# api.add_resource(Pizzas, '')


@RX.route('/pizzas/<int:id>')
class Pizzas_by_id(Resource):
        def get(sefl,id):
            pizza = Pizza.query.filter_by(id=id).first()

            if pizza:
                 pizza_dict = pizza.to_dict()
                
                 return make_response(pizza_dict,200)






@RX.route('/restaurant_pizzas')
class RestaurantPpizzas(Resource):
     def post(self):
        restaurant_pizza = RestaurantPizza(
            price =request.form.get('price'),
            pizza_id= request.form.get('pizza_id'),
            restaurant_id=request.form.get('restaurant_id'),
        
        )
        db.session.add(restaurant_pizza)
        db.session.commit()


        rp_dict = restaurant_pizza.to_dict()
        if rp_dict:
            return make_response(rp_dict['pizza'],201)
        else:
            response ={"errors": ["validation errors"] }
            return make_response(restaurant_pizza, 404)


          




