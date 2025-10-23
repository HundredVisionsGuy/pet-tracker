"""
dog.py
by Chris Winikka
A Dog object based on the Pet
"""
from pet import Pet

class Dog(Pet):
    count = 0
    def __init__(self, name, breed, age):
        super().__init__()

        # add to the count of pets
        Pet.count += 1
        Dog.count += 1

        # Set instance attributes
        self.name = name
        self.breed = breed
        self.age = age
    
    def __str__(self):
        representation = "\nSpecies: Cat\n"
        representation += f"\nName: {self.name}\n"
        representation += f"Breed: {self.breed}\n"
        representation += f"Age: {self.age}\n"
        representation += f"1 of {Dog.count} dogs.\n"
        representation += f"1 of {Pet.count} pets."
        return representation


if __name__ == "__main__":
    # Add some dogs
    fluffy = Dog("Fluffy", "Terrier", 4)
    sandy = Dog("Sandy", "Cocker Spaniel", 3)

    # Print dog information
    print(fluffy)
    print(sandy)
    name_of_dog = fluffy.get_name()
