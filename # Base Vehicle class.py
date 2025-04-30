# Base Vehicle class
class Vehicle:
    def __init__(self, brand, model, year):
        self._brand = brand         # Encapsulated attribute
        self._model = model
        self._year = year
        self._is_running = False

    # Getter for brand (encapsulation)
    @property
    def brand(self):
        return self._brand

    # Setter for year with validation
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if 1886 <= value <= 2025:  # Assuming vehicles start from 1886 (first car)
            self._year = value
        else:
            raise ValueError("Year must be between 1886 and 2025")

    # Method to toggle running status
    def toggle_engine(self):
        self._is_running = not self._is_running
        status = "running" if self._is_running else "stopped"
        return f"{self._brand} {self._model} engine is now {status}."

    # Abstract-like method for movement (to be overridden)
    def move(self):
        return f"{self._brand} {self._model} is moving generically."

    # Method to describe the vehicle
    def describe(self):
        return f"{self._year} {self._brand} {self._model}"

# Derived class for Car
class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    # Polymorphic move method
    def move(self):
        return f"{self._brand} {self._model} is driving on the road! 🚗"

    # Additional method specific to Car
    def honk(self):
        return f"{self._brand} {self._model} goes Beep Beep!"

# Derived class for Plane
class Plane(Vehicle):
    def __init__(self, brand, model, year, max_altitude):
        super().__init__(brand, model, year)
        self.max_altitude = max_altitude

    # Polymorphic move method
    def move(self):
        return f"{self._brand} {self._model} is flying at {self.max_altitude} feet! ✈️"

    # Additional method specific to Plane
    def land(self):
        return f"{self._brand} {self._model} has landed safely."

# Demonstration of the classes
def main():
    # Create instances of different vehicles
    sedan = Car("Toyota", "Camry", 2020, 4)
    jet = Plane("Boeing", "747", 2015, 35000)
    generic_vehicle = Vehicle("Generic", "Model X", 2010)

    # Store vehicles in a list to demonstrate polymorphism
    vehicles = [sedan, jet, generic_vehicle]

    # Demonstrate polymorphism with move()
    print("Vehicles Moving:")
    for vehicle in vehicles:
        print(vehicle.move())

    # Demonstrate other methods
    print("\nVehicle Descriptions:")
    for vehicle in vehicles:
        print(vehicle.describe())

    # Demonstrate specific methods and encapsulation
    print("\nSpecial Actions:")
    print(sedan.honk())
    print(jet.land())
    print(generic_vehicle.toggle_engine())

    # Demonstrate getter and setter
    print(f"\nAccessing {sedan.brand}'s year: {sedan.year}")
    sedan.year = 2022
    print(f"Updated {sedan.brand}'s year: {sedan.year}")

if __name__ == "__main__":
    main()