# Information:
# Program type: Text-adventure Game
# Project start date: 9-20-2017


### notes about my code ###
# All variables that are used specifically for lists will be suffixed with '_lst'
# For example Fruit_lst = ['apple', 'orange', 'grape']

# I use lots of external .txt files to draw descriptors, names, etc.
# you can find these files in the 'Resources' folder.
# each set of lists is clearly named and in clearly marked folders. (I hope...)

### end of notes ###

import time
import random
import os
import shutil
import sys

# Detects if the user's input for their name includes a number.
def has_numbers(inputString):
    return any (char.isdigit() for char in inputString)

# initializes character and location classes
class Character():
    def __init__(self):
        self.name = ""
        self.health = "100"
        self.gender = ""

class LocationNames():
    def __init__(self):
        self.name = ""
        self.type = ""
        self.weather = ""

# simplifies text alignment
def align_center(s):
    return s.center(shutil.get_terminal_size().columns)

# this function clears the screen when nesseary.
def clear():
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')

# links the classes "Character" and "LocationNames" to enable variable instances.
User = Character()
MainCity = LocationNames()

# randomly selects and assigns a weather adjective for an associated city.
weather_lst = open("Resources/Weather/weatherMain.txt").read().splitlines()
MainCity.weather = random.choice(weather_lst)

# randomly selects a city name from the .txt file and assigns it.
cities_lst = open("Resources/Cities&Towns/city_names.txt").read().splitlines()
MainCity.name = random.choice(cities_lst)

# classifies the established settlement as a "town", "village", "city", etc.
city_class_lst = open("Resources/Cities&Towns/city_type.txt").read().splitlines()
MainCity.type = random.choice(city_class_lst)

# randomized gatekeeper name
gatekeeper_name_lst = open("Resources/characters/gatekeepers.txt").read().splitlines()
gatekeeper_name = random.choice(gatekeeper_name_lst)

# load the logo and display when called as a variable
logo = open("Resources/logos/logo_main.txt").read()

# define other variables
start_check = ""
check_quit = ""
error = "Invalid input, Please try again."

# check if the user would like to start the game.
while start_check is "":
    check_quit = ""
    start_check = input("Would you like to begin? (Yes or No): ")
    if start_check not in {'Yes','yes','y','YES','no','NO','No','n'}:
        print(error)
        start_check = ""
    elif start_check in {'YES','Yes','yes','y'}:
        break
#   if no, verify with 'are you sure?' before terminating.
    elif start_check in {'no','NO','No','n'}:
        while check_quit is "":
            check_quit = input("Are you sure you wish to quit? (Yes or No): ")
            if check_quit not in ['Yes','yes','y','YES','no','NO','No','n']:
                print(error)
                check_quit = ""
            elif check_quit in ['YES','Yes','yes','y']:
                quit()
#    if they decide they DON'T want to quit, remain in the loop by setting "start_check" back to the "{empty}" state.
            elif check_quit in ['no','NO','No','n']:
                start_check = ""
                break

# when beginging the game display the logo
print("Welcome, to... \n" + logo)
time.sleep(5)
clear()

# I want the following to be replaced with a script segment
# that randomly generates a description of the weather, the town, and details of the town.
# Will draw from .txt files and randomize to variables in classes for infinite combinations.
print(align_center("You slowly and exhaustedly crest the hill, a " + MainCity.type + " appearing on the horizon."))
time.sleep(3)
print(align_center("You know the place in front of you... it\'s " + MainCity.name + "." ))

# need to create a variable in which the value changes based on the weather.
# I.E. it wouldnt make sense to take shelter on a sunny day.
time.sleep(3)
print(align_center("The weather is " + MainCity.weather + ", it might be a good idea to stop and rest."))
time.sleep(3)

# here, MainCity.weather should be changed to a new variable that would dislay a chracteristic of MainCity.weather
print(align_center("As you approach you see a gate keeper come out to meet you in the " + MainCity.weather +" weather."))



print (align_center("Well met traveler! I am " + gatekeeper_name + ", I keep tabs on who comes and goes here."))
time.sleep(2)
while User.name == "":
    User.name = input("\n What is your name? (Enter name): ")

    if has_numbers(User.name) == True:
        print ("That's not a valid name. Please don't use numbers.")
        time.sleep(2)
        User.name = ""
    elif has_numbers(User.name) == False:
        print (align_center("Ah! Fair travels " + User.name + "!"))
        break

time.sleep(1)
print(align_center("Your clothes obscure you..."))
time.sleep(1)
print (align_center("and your hood makes it hard for me to see your face..."))

while User.gender == "":
    User.gender = str(input("What gender are you? (boy or girl?): "))
    if User.gender not in {'boy', 'BOY', 'Boy', 'girl', 'GIRL', 'Girl'}:
        print (align_center("Come now, quit being shy about your gender child!"))
        User.gender = ""
        time.sleep(1)


#   Generalizing multiple possible responses, and then contining story based on that response
    elif User.gender in {'boy', 'BOY', 'Boy'}:
        User.gender = "boy"
        time.sleep(1)
        print("Oh? Well, tread carefully around here Boy, the garrison is snapping up young lads by the ton...")
        break
    elif User.gender in {'girl', 'GIRL', 'Girl'}:
        User.gender = "girl"
        time.sleep(1)
        print("Oh? And what's a lady like yourself doin\' traveling alone?")
        break
