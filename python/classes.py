import random

"""
code sample demonstrating classes

four core aspects:
    1. class: blueprint declared using class keyword
    2. object/instance: actual thing built using the template
    3. attributes: variables that store data / properties
    4. methods: functions inside of class that describe actions
"""

# create the class
class Hobbit:
    # this will run everytime we create a new hobbit character (object)
    def __init__(self, name, weapon):
        self.name = name # every hobbit will have a name
        self.weapon = weapon # and a weapon
        self.hp = 100 

    # hobbits can often DO (a method / an action)
    def greet(self):
        hobbit_quotes = [
            "I can't go back. Not to the Shire. It won't seem the same; for I shall not be the same.",
            "We’ve had one, yes, but what about second breakfast?",
            "It is a wide world after all; things will go on anyway."
        ]
        print(f"{self.name} says: {random.choices(hobbit_quotes)[0]}")

    def use_weapon(self):
        print(f"{self.name} uses their {self.weapon}!")

    def takes_damage(self):
        self.hp -= 20
        print(f"{self.name} takes damange: energy is now {self.hp}")


# STEP 2: Use the mold to create real characters (objects)!
frodo = Hobbit("Frodo", "a small sword")
sam = Hobbit("Sam", "a frying pan")

print("* -- meet our hobbits -- *")
frodo.greet()
sam.greet()

print("* -- hobbits doing things -- *")
frodo.use_weapon()
frodo.takes_damage()

sam.use_weapon()
sam.takes_damage()
