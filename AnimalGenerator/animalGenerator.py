import random

class Animal:
    # Define what happens when a new animal object instance is created
    def __init__(self, animal_type, animal_name):
        self.__animal_type = animal_type
        self.__name = animal_name

        # Pick a number between 1 and 3
        random_number = random.randint(1, 3)

        # Set the animal's mood based on the random number
        if random_number == 1:
            self.__mood = "happy"
        elif random_number == 2:
            self.__mood = "hungry"           
        elif random_number == 3:
            self.__mood = "sleepy"
        
    # Return the animal's type
    def get_animal_type(self):
        return self.__animal_type

    # Return the animal's name
    def get_name(self):
        return self.__name

    # Return the animal's mood
    def check_mood(self):
        return self.__mood 

print("Welcome to the animal generator!")
print("This program creates Animal objects")


while (True):
    #prompt the user to make an animal or bird
    print()
    print ("Would you like to create a mammal or bird?")
    print("1. Mammal")
    print("2. Bird")
    animalChoice = input("Which would you like to create? ")

    if animalChoice == 1:
        mammalType = input("What type of mammal would you like to create? ")
        mammalName = input("What is the mammals name? ")
        mamalHair = input("What color is the mammal's hair? ")
        
    else:
        birdType = input("What type of bird would you like to create? ")
        birdName = input("What is the bird name? ")
        birdFly = input("Can the bird fly? ")
        #initialize 

    anotherAnimal = input("Would you like to add more animals (y/n) ")
    if choice != "y":
            break
       
#while dictionary print name the animal is emotion
