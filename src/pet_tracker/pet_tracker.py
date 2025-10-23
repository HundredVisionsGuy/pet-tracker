"""
Pet Tracker
by Chris Winikka
Include a short description of your project.
"""
from dog import Dog
from cat import Cat


def main():
    print("Welcome")
    print("This is my Pet Tracking program")

    # Create some dog objects
    luna = Dog("Luna", "Standard Poodle", 7)
    print(luna)
    sandy = Dog("Sandy", "Cocker Spaniel", 3)
    print(sandy)

    # Create a cat
    morrisey = Cat("Morrisey", "Rag Doll", 3)
    print(morrisey)


if __name__ == "__main__":
    main()
