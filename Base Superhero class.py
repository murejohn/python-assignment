 Base Superhero class
class Superhero:
    def __init__(self, name, power_level, city):
        self._name = name           # Encapsulated attribute
        self._power_level = power_level
        self._city = city
        self._is_active = True

    # Getter for name (encapsulation)
    @property
    def name(self):
        return self._name

    # Setter for power_level with validation
    @property
    def power_level(self):
        return self._power_level

    @power_level.setter
    def power_level(self, value):
        if value >= 0:
            self._power_level = value
        else:
            raise ValueError("Power level cannot be negative")

    # Method to toggle active status
    def toggle_active(self):
        self._is_active = not self._is_active
        status = "active" if self._is_active else "retired"
        return f"{self._name} is now {status}!"

    # Abstract-like method for movement (to be overridden)
    def move(self):
        return f"{self._name} is moving in a generic way."

    # Method to describe the superhero
    def describe(self):
        return f"{self._name}, Power Level: {self._power_level}, Protects: {self._city}"

# Derived class for Flying Superhero
class FlyingHero(Superhero):
    def __init__(self, name, power_level, city, max_altitude):
        super().__init__(name, power_level, city)
        self.max_altitude = max_altitude

    # Polymorphic move method
    def move(self):
        return f"{self._name} is soaring through the skies at {self.max_altitude} feet! ✈️"

    # Additional method specific to FlyingHero
    def increase_altitude(self, increase):
        self.max_altitude += increase
        return f"{self._name} can now fly up to {self.max_altitude} feet!"

# Derived class for Speedster Superhero
class SpeedsterHero(Superhero):
    def __init__(self, name, power_level, city, max_speed):
        super().__init__(name, power_level, city)
        self.max_speed = max_speed

    # Polymorphic move method
    def move(self):
        return f"{self._name} is zooming at {self.max_speed} mph! 🏃‍♂️"

    # Additional method specific to SpeedsterHero
    def boost_speed(self, boost):
        self.max_speed += boost
        return f"{self._name}'s speed increased to {self.max_speed} mph!"

# Demonstration of the classes
def main():
    # Create instances of different superheroes
    sky_lad = FlyingHero("Sky Lad", 85, "Metro City", 30000)
    bolt = SpeedsterHero("Bolt", 90, "Speedville", 600)
    generic_man = Superhero("Generic Man", 50, "Normal Town")

    # Store heroes in a list to demonstrate polymorphism
    heroes = [sky_lad, bolt, generic_man]

    # Demonstrate polymorphism with move()
    print("Heroes Moving:")
    for hero in heroes:
        print(hero.move())

    # Demonstrate other methods
    print("\nHero Descriptions:")
    for hero in heroes:
        print(hero.describe())

    # Demonstrate specific methods and encapsulation
    print("\nSpecial Abilities:")
    print(sky_lad.increase_altitude(5000))
    print(bolt.boost_speed(100))
    print(generic_man.toggle_active())

    # Demonstrate getter and setter
    print(f"\nAccessing {sky_lad.name}'s power level: {sky_lad.power_level}")
    sky_lad.power_level = 95
    print(f"Updated {sky_lad.name}'s power level: {sky_lad.power_level}")

if __name__ == "__main__":
    main()