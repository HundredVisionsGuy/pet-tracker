"""
pet.py
By Chris Winikka
A base class for all pets.
"""


class Pet():
    count = 0

    def __init__(self):
        self.name = ""
        self.breed = ""
        self.age = 1

    def get_name(self):
        return self.name
    
    def get_breed(self):
        return self.breed

    def get_age(self):
        return self.age
    
    



if __name__ == "__main__":
    print(Pet.count)
