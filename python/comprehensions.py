"""
title: comprehensions sample
author: jacob murray
description: code sample to demonstration list, dict comprehensions
"""

# list comprehensions
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

###################
#  using a for loop
###################

even_numbers = []

for number in list_1: 
    print(number)
    if number % 2 == 0:
        print(f'{number} is even')
        even_numbers.append(number)
    else: 
        print(f'{number} is odd')

print(even_numbers)

#####################
# list comprehension!
#####################

## [expression for member in iterable]
## [expression for member in iterable if conditional]

list_comp = [num for num in list_1 if num % 2 == 0]
print(list_comp)

[
    num # expressions
    for num in list_1 # if loop
    if num % 2 == 0 # conditional
]


# manipulating returns!
fruit_list = ['apple', 'banana', 'cherry', 'peach']
fruit_comp = [x if x != "apple" else "switch" for x in fruit_list]
fruit_comp

###########################
# dictionary comprehensions
###########################

# creating dictionaries from iterables
genres = ["rock", "classical", "pop", 'rap']
{genre.upper(): genre.lower() for genre in genres}


{"packages": 
    {"stock_code": 1,
     "weight": "Columbus",
     "height": 140
    }



}

# comps with dictionaries
# say i'm wanting to discount all my products by 10%
products = {
    "iPod": 150,
    "TV": 700,
    "record player": 89,
    "banana": 1,
}
promos = {product: round(price * 0.90, 2) for product, price in products.items()}
promos
