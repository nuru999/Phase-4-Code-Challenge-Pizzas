#!/usr/bin/env python3
import random
from random import randint, choice as rc

from faker import Faker


from api import app
from api.models import db, Restaurant,Pizza,RestaurantPizza

fake = Faker()

with app.app_context():
    ''' ----------------R E S T A U R A N T-------------- '''
    Restaurant.query.delete()    
    # using list comprehension to populate
    foods = ['foods','peverages','bites','specials','dessert','breakfast','Pizzas','Burgers','appetizers',]
    restaurant_list = [Restaurant(
        name = fake.unique.company() + f" {random.choice(foods)}",
        address = fake.address()  )
    for i in range(15)
    ]
    db.session.add_all(restaurant_list)
    db.session.commit()


    '''---------------- P I Z Z A --------------------------'''
    Pizza.query.delete()
    # pizzas and their ingredients
    pizza_data = {
    "Pizza Margherita": ["Tomato Sauce", "Mozzarella Cheese", "Fresh Basil", "Olive Oil"],
    "Pepperoni Pizza": ["Tomato Sauce", "Mozzarella Cheese", "Pepperoni Slices"],
    "Hawaiian Pizza": ["Tomato Sauce", "Mozzarella Cheese", "Ham", "Pineapple"],
    "Vegetarian Pizza": ["Tomato Sauce", "Mozzarella Cheese", "Bell Peppers", "Mushrooms", "Onions", "Olives"],
    "BBQ Chicken Pizza": ["BBQ Sauce", "Mozzarella Cheese", "Grilled Chicken", "Red Onions", "Cilantro"],
    "Meat Lover's Pizza": ["Tomato Sauce", "Mozzarella Cheese", "Pepperoni", "Sausage", "Bacon", "Ground Beef"],
    "Supreme Pizza": ["Tomato Sauce", "Mozzarella Cheese", "Pepperoni", "Sausage", "Bell Peppers", "Onions", "Olives"],
    "White Pizza": ["Olive Oil", "Garlic", "Mozzarella Cheese", "Ricotta Cheese", "Parmesan Cheese"],
    "Buffalo Chicken Pizza": ["Buffalo Sauce", "Mozzarella Cheese", "Grilled Chicken", "Red Onions", "Blue Cheese Dressing"],
    "Pesto Pizza": ["Pesto Sauce", "Mozzarella Cheese", "Cherry Tomatoes", "Fresh Basil"],
    "Mushroom Pizza": ["Tomato Sauce", "Mozzarella Cheese", "Mushrooms", "Garlic", "Thyme"],
    "Four Cheese Pizza": ["Tomato Sauce", "Mozzarella Cheese", "Fontina Cheese", "Parmesan Cheese", "Gorgonzola Cheese"],
    "Bacon and Egg Pizza": ["Olive Oil", "Mozzarella Cheese", "Bacon", "Eggs", "Chives"],
    "Spinach and Feta Pizza": ["Tomato Sauce", "Mozzarella Cheese", "Spinach", "Feta Cheese", "Garlic"],
    "Barbecue Bacon Pizza": ["BBQ Sauce", "Mozzarella Cheese", "Bacon", "Red Onions", "Cilantro"]
    }

    pizza_images = [
            ' https://img.freepik.com/free-photo/freshly-italian-pizza-with-mozzarella-cheese-slice-generative-ai_188544-12347.jpg',
            'https://img.freepik.com/premium-photo/pizza-black-background-with-lot-smoke-flames_856795-7657.jpg?w=2000 ',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTt_ygZJzyQLzNMc7-as8hn509cNW00ywtO0mtokJKr&s ',
            'https://t3.ftcdn.net/jpg/05/60/70/82/360_F_560708240_pMZPOuSfvblWGRoaiZFLT4wiFTzQPwQe.jpg ',
            'https://images.unsplash.com/photo-1513104890138-7c749659a591?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8fA%3D%3D&w=1000&q=80',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBKO880ew0WLj8NVk0KAixAawN4ZtFWfPsB8U3suTafQc8gYgoH_rSxUYPyp9VIad4k_k&usqp=CAU',
            'https://t4.ftcdn.net/jpg/00/71/27/57/360_F_71275778_e4d7y5ADlApa9g0A4tm0Jqc5Q3FznuGI.jpg',
            'https://i.etsystatic.com/27713397/r/il/b82145/4266698419/il_fullxfull.4266698419_7xfm.jpg',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrDaIPHlALcF8P_BOc1x51G8GTGlTbIvTBTg&usqp=CAU',
            'https://media.istockphoto.com/id/489809469/photo/bbq-chicken-pizza.jpg?s=612x612&w=0&k=20&c=kB3xRU4-A7fJ9iYpIzlOqSiLX4f6OIath45yFOmqjxQ=',
            
    ]

    pizza_name = []
    pizza_ingredient= []
   
    for pizza in (pizza_data.items()):
        pizza_name.append(pizza[0])
        pizza_ingredient.append(",".join(pizza[1]))

   
    pizza_list = [Pizza(
        name =pizza_name[i],
        ingredients=pizza_ingredient[i],
        image = random.choice(pizza_images)
        
        )
        
        for i in range(15)
    ]

    db.session.add_all(pizza_list)
    db.session.commit()


    '''------------ P I Z Z A----R E S T A U R A N T  -------------'''
    RestaurantPizza.query.delete()
    restaurant_pizza_list = []
    for rest in restaurant_list:
        for i in range(randint(1,15)):
            rp = RestaurantPizza(
                price =(random.randint(1,30)),
                restaurant = rest,
                pizza = rc(pizza_list)
            )
            restaurant_pizza_list.append(rp)

    db.session.add_all(restaurant_pizza_list)
    db.session.commit()


    restaurant1=(restaurant_list[0])
    rp=(restaurant_pizza_list[0])
    pizza1=(pizza_list[0])
    print(restaurant1.pizzas[0].rest_pizza_association[0].price) 
    # print(pizza1.restaurants[0].pizza)
  