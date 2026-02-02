# Define a simple class
class Dog:
    # A class attribute, shared by all instances
    species = "canine"

    # The __init__ method (constructor) initializes new instances
    def __init__(self, name, age):
        # Instance attributes, unique to each instance
        self.name = name
        self.age = age

    # An instance method defines a behavior
    def bark(self):
        return f"{self.name} says woof!"

# Create instances (objects) of the class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

# Access attributes and call methods
print(f"{dog1.name} is {dog1.age} years old and is a {dog1.species}.")
print(dog2.bark())
