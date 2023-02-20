from typing import List
import requests
from api import Character, Planet
# import json

def url(route: str):
    return f"http://127.0.0.1:8000{route}"


##########################
# Functions for main app #
##########################

def check_input(choice, a, b):
    if not str.isdigit(choice):
        return False
    elif int(choice) not in range(a, b):
        return False
    else:
        return True

def print_person(ret):
    for i in ret:
        print(f"ID: {i['id']} | Name: {i['name']} | Description: {i['description']} | Age: {i['age']} | Home Planet: {i['home_planet']}")
    print("")    

def print_planet(ret):
    for i in ret:
        print(f"ID: {i['id']} | Name: {i['name']} | Sector: {i['sector']}")
    print("")    


#######################
# Simple get requests #
#######################

def get_planets():
    res = requests.get(url("/planets/get_planets"))
    # Transforn result to json-object using .json() (from requests package)
    data = res.json() 
    return data 
   
def get_characters():
    res = requests.get(url("/characters/get_characters"))
    data = res.json()
    return data
            

################################
# get requests with conditions #
################################

def get_planet_by_name(name: str):
    res = requests.get(url(f"/planets/get_planet/{name}"))
    data = res.json()
    return data

def get_character_by_name(name: str):
    res = requests.get(url(f"/characters/get_character/{name}"))
    data = res.json()
    return data

def get_character_by_planet(planet: str):
    res = requests.get(url(f"/character/get_character_by_planet/{planet}"))
    data = res.json()
    return data

def get_oldest_character():
    res = requests.get(url("/characters/get_oldest"))
    data = res.json()
    return data

def get_planets_by_sector(sector: str):
    res = requests.get(url(f"/planets/get_by_sector/{sector}"))
    data = res.json()
    return data

def get_planet_duplicates():
    res = requests.get(url("/planets/get_duplicates"))
    data = res.json()
    return data

def get_character_duplicates():
    res = requests.get(url("/characters/get_duplicates"))
    data = res.json()
    return data

########################
# Simple post requests #
########################


def add_planet():
    name = input("Name: ")
    sector = input("Sector: ")
    # Create object with the input values
    new_planet = Planet(name=name, sector=sector)
    # Send new_planer as a json into the ur and the method add_planet()
    requests.post(url(f"/planets/add_planet"), json=new_planet.dict())

def add_character():
    name = input("Name: ")
    description = input("Description: ")
    age = input("Age: ")
    homeplanet = input("Home planet: ")
    new_character = Character(name=name, description=description, age=age, home_planet=homeplanet)
    requests.post(url(f"/characters/add_character"), json=new_character.dict())


####################
# Delete requestes #
####################


def delete_character(char: List[Character]):
    name = input("What character would you like to delete?: ")
    # See if name is in table
    found = False
    for i in char:
        if i['name'] == name:
            found = True
    
    if found == False:
        print("Invalid entry")
        input("")
        return
    else:
        requests.delete(url(f"/characters/delete_character/{name}"))

def delete_planet(planet : List[Planet]):
    name = input("What planet would you like to delete?: ")

    found = False
    for i in planet:
        if i['name'] == name:
            found = True  
    if found == False:
        print("invalid entry")
        input("")
        return 
    else: 
        requests.delete(url(f"/planets/delete_planet/{name}"))
    
def remove_duplicate_planets():
    requests.delete(url("/planets/remove_duplicates"))

def remove_duplicate_characters():
    requests.delete(url("/characters/remove_duplicates"))


################
# Put requests #
################


# to modify, first run get_characters to get the right one
def modify_character(characters: List[Character]):
    old_character = input("What is the name of the character you would like to modify?: ")
    found = False
    for i in characters:
        if i['name'] == old_character:
            found = True
            break          
    if found == False:
        print("Invalid entry")
        input("")
        return
    else:
        print_person(get_character_by_name(old_character))
        new_name = input("New name (leave empty if same): ")
        new_description = input("New description (leave empty if same): ")
        new_age = input("New age (leave empty if same): ")
        new_home_planet = input("New home planet (leave empty if same): ")

        if not new_name:
            new_name = i['name']
        
        if not new_age:
            new_age = i['age']

        if not new_description:
            new_description = i['description']

        if not new_home_planet:
            new_home_planet = i['home_planet']


    new_character = Character(name=new_name, description=new_description, age=new_age, home_planet=new_home_planet)
    requests.put(url(f"/characters/modify_character/{old_character}"), json=new_character.dict())

def modify_planet(planets: List[Planet]):
    old_planet = input("What planet would you like to modify?").strip()
    found = False
    for i in planets:
        if i['name'] == old_planet:
            found = True
            break
        
    if found == False:
        print("Invalid entry")
        input("")
        return
    else:       
        print_planet(get_planet_by_name(old_planet))     
        new_name = input("New name (leave empty if same): ")
        new_sector = input("New sector (leave empty if same): ")

        if not new_name:
            new_name = i['name']
        if not new_sector:
            new_sector = i['sector']
    new_planet = Planet(name=new_name, sector=new_sector)
    requests.put(url(f"/planets/modify_planet/{old_planet}"), json=new_planet.dict())