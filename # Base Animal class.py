# Base Animal class
class Animal:
    def __init__(self, species, name, age):
        self._species = species     # Encapsulated attribute
        self._name = name
        self._age = age
        self._is_active = True

    # Getter for name (encapsulation)
    @property
    def name(self):
        return self._name

    # Setter for age with validation
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age cannot be negative")

    # Method to toggle active status
    def toggle_activity(self):
        self._is_active = not self._is_active
        status = "active" if self._is_active else "resting"
        return f"{self._name} the {self._species} is now {status}."

    # Abstract-like method for movement (to be overridden)
    def move(self):
        return f"{self._name} the {self._species} is moving generically."

    # Method to describe the animal
    def describe(self):
        return f"{self._name}, a {self._age}-year-old {self._species}"

# Derived class for Bird
class Bird(Animal):
    def __init__(self, species, name, age, wingspan):
        super().__init__(species, name, age)
        self.wingspan = wingspan

    # Polymorphic move method
    def move(self):
        return f"{self._name} the {self._species} is flying with a {self.wingspan}-cm wingspan! 🦅"

    # Additional method specific to Bird
    def chirp(self):
        return f"{self._name} chirps melodiously!"

# Derived class for Fish
class Fish(Animal):
    def __init__(self, species, name, age, max_depth):
        super().__init__(species, name, age)
        self.max_depth = max_depth

    # Polymorphic move method
    def move(self):
        return f"{self._name} the {self._species} is swimming at depths up to {self.max_depth} meters! 🐠"

    # Additional method specific to Fish
    def bubble(self):
        return f"{self._name} blows bubbles in the water!"

# Demonstration of the classes
def main():
    # Create instances of different animals
    eagle = Bird("Eagle", "Skyler", 5, 200)
    tuna = Fish("Tuna", "Bubbles", 3, 100)
    generic_animal = Animal("Mammal", "Generic", 4)

    # Store animals in a list to demonstrate polymorphism
    animals = [eagle, tuna, generic_animal]

    # Demonstrate polymorphism with move()
    print("Animals Moving:")
    for animal in animals:
        print(animal.move())

    # Demonstrate other methods
    print("\nAnimal Descriptions:")
    for animal in animals:
        print(animal.describe())

    # Demonstrate specific methods and encapsulation
    print("\nSpecial Actions:")
    print(eagle.chirp())
    print(tuna.bubble())
    print(generic_animal.toggle_activity())

    # Demonstrate getter and setter
    print(f"\nAccessing {eagle.name}'s age: {eagle.age}")
    eagle class Animal:
    def __init__(self, species, name, age):
        self._species = species     # Encapsulated attribute
        self._name = name
        self._age = age
        self._is_active = True

    # Getter for name (encapsulation)
    @property
    def name(self):
        return self._name

    # Setter for age with validation
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age cannot be negative")

    # Method to toggle active status
    def toggle_activity(self):
        self._is_active = not self._is_active
        status = "active" if self._is_active else "resting"
        return f"{self._name} the {self._species} is now {status}."

    # Abstract-like method for movement (to be overridden)
    def move(self):
        return f"{self._name} the {self._species} is moving generically."

    # Method to describe the animal
    def describe(self):
        return f"{self._name}, a {self._age}-year-old {self._species}"

# Derived class for Bird
class Bird(Animal):
    def __init__(self, species, name, age, wingspan):
        super().__init__(species, name, age)
        self.wingspan = wingspan

    # Polymorphic move method
    def move(self):
        return f"{self._name} the {self._species} is flying with a {self.wingspan}-cm wingspan! 🦅"

    # Additional method specific to Bird
    def chirp(self):
        return f"{self._name} chirps melodiously!"

# Derived class for Fish
class Fish(Animal):
    def __init__(self, species, name, age, max_depth):
        super().__init__(species, name, age)
        self.max_depth = max_depth

    # Polymorphic move method
    def move(self):
        return f"{self._name} the {self._species} is swimming at depths up to {self.max_depth} meters! 🐠"

    # Additional method specific to Fish