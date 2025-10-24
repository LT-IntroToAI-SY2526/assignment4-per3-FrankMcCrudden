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

    def __init__(self, fur_color = "black", name = "no name", age = "1", favorite_food = "kibble"):
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
    def birthday(self):
        """Celebrate the dog's birthday"""
        self.age += 1
        print(f"Celebrating {self.name}'s birthday! They are now {self.age} years old")
    def change_favorite_food(self, new_food):
        """Change the favorite food of the dog"""
        old_food = self.favorite_food
        self.favorite_food = new_food
        print(f"{self.name} use to love {old_food} and now loves {self.favorite_food}")
        

my_dog = Dog("black", "logan", 9, "salmon")
enggy_dog = Dog("black and white", "pelchin", 13, "rice")
defualt_dog = Dog()
aaron_dog = Dog("peach and white", "Dumbo", 1, "anything edible")
 
print(my_dog)
print(enggy_dog)
print()
print(enggy_dog.bark)
print()
print(defualt_dog)
print(aaron_dog)
aaron_dog.birthday
print(aaron_dog)