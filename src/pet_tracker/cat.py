"""
"""

from pet import Pet

class Cat(Pet):
    count = 0

    def __init__(self, name, breed, age):
        super().__init__()
        self.name = name
        self.breed = breed
        self.age = age
        Cat.count += 1
        Pet.count += 1

    def __str__(self):
        representation = "\nSpecies: Cat\n"
        representation += f"Name: {self.name}\n"
        representation += f"Breed: {self.breed}\n"
        representation += f"Age: {self.age}\n"
        representation += f"1 of {Cat.count} cats.\n"
        representation += f"1 of {Pet.count} pets."
        return representation


if __name__ == "__main__":
    morrisey = Cat("Morrisey", "Rag Doll", 3)
    print(morrisey)
