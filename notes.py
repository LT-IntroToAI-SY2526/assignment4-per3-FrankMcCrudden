# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    """A simple Dog class to learn OOP (Object Oriented Language)

    Atrributes:
        fur_color - the color of the dogs fur
        name - the name of the dog
        age - the age of the dog
        favorite_food - the dog's favorite food
    """

    def __init__(self, fur_color, name, age, favorite_food):
        """Initialize a new dog with fur_color, name, age,
        and favorite_food
        """
        self.fur_color = fur_color
        self.name = name
        self.age = age
        self.favorite_food = favorite_food
    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.fur_color} dog who's favorite food is {self.favorite_food}"

    def bark(self):
        """Make the dog bark"""
        return f"{self.name} says Woof, Woof!!"
        

my_dog = Dog("black", "logan", 9, "salmon")
enggy_dog = Dog("black and white", "pelchin", 13, "rice")

print(my_dog)
print(enggy_dog)
print()
print(enggy_dog.bark)