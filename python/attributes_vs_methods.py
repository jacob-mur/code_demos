"""
demonstrating the difference between attributes vs methods
attributes: 
    - variable belonging to an object (metadata)
    - information or state of an object
    - no parentheses 
    - can have class attribute (data shared by entire class)
    - can have instance attributes (data specific to instance of class)

basic rule:
    - attribute = a NOUN describing the object
    - method = a VERB the object can perform

important note:
- functions and methods are closely related, but not the same
- functions are defined outside of any class, methods are defined inside object/class
- function: function_name(), method: object.method name
- data acess: 
    - functions only operate on arguments passed
    - methods can can access / modify internal state of an object

technical nuance:
- in Python 3, difference between accessing function via class name vs through class instance
"""

class Car: 
    """a simple class to demonstrate attributes and methods"""

    # attribute for entire class
    wheels = 4

    # instance attributes
    def __init__(self, brand, model, year, gas_type, mpg):
        self.brand = brand     
        self.model = model 
        self.year = year
        self.gas_type = gas_type
        self.mpg = mpg

    # instance method building on attributes
    def car_info(self):
        return(f'{self.brand} {self.model}')

    # method calculating how many gallons of gas needed for trip
    def road_trip(self, miles):
        return f'your trip will take about {round(miles / self.mpg, 2)} gallons of gas'


my_car = Car('VW', 'JETTA', 2024, 'Hybrid', 76)
type(my_car)

# testing attribute
my_car.wheels
my_car.brand
my_car.model

# testing methods
my_car.car_info()
my_car.road_trip(100)







