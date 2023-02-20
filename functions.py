from typing import List
import requests
from api import Character, Planet
import os

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

def get_planet_by_id(id: int):
    res = requests.get(url(f"/planets/get_planet_by_id/{id}"))
    data = res.json()
    return data

def get_character_by_id(id: int):
    res = requests.get(url(f"/characters/get_character_by_id/{id}"))
    data = res.json()
    return data

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


def delete_character(id):
    requests.delete(url(f"/characters/delete_character/{id}"))

def delete_planet(id):
    requests.delete(url(f"/planets/delete_planet/{id}"))
    
def remove_duplicate_planets():
    requests.delete(url("/planets/remove_duplicates"))

def remove_duplicate_characters():
    requests.delete(url("/characters/remove_duplicates"))


################
# Put requests #
################


def alter_entry(entry_type, x, mod_or_delete, thing_to_print):
    if len(entry_type) > 1:
        os.system('cls')
        print(f"There is more than one {x} with that name.")
        thing_to_print(entry_type)
        id = input(f"Type the ID of the {x} you'd like to alter: ")
        mod_or_delete(id)
        input("Complete")
    elif len(entry_type) == 1:
        id = entry_type[0]['id']
        mod_or_delete(id)
        input("Complete")
    else: 
        print("Invalid entry")
        input("")
        return  
    
# to modify, first run get_characters to get the right one
def modify_character(id: int):
    char = get_character_by_id(id)
    print_person(char)
    new_name = input("New name (leave empty if same): ")
    new_description = input("New description (leave empty if same): ")
    new_age = input("New age (leave empty if same): ")
    new_home_planet = input("New home planet (leave empty if same): ")

    if not new_name:
        new_name = char[0]['name']
    
    if not new_age:
        new_age = char[0]['age']

    if not new_description:
        new_description = char[0]['description']

    if not new_home_planet:
        new_home_planet = char[0]['home_planet']
        
    new_character = Character(name=new_name, description=new_description, age=new_age, home_planet=new_home_planet)
    requests.put(url(f"/characters/modify_character/{id}"), json=new_character.dict())

def modify_planet(id: int):
    plan = get_planet_by_id(id)
    print_planet(plan)
    new_name = input("New name (leave empty if same): ")
    new_sector = input("New sector name (leave empty if same): ")

    if not new_name:
        new_name = plan[0]['name']
    if not new_sector:
        new_sector = plan[0]['sector']
    new_planet = Planet(name=new_name, sector=new_sector)
    requests.put(url(f"/planets/modify_planet/{id}"), json=new_planet.dict())
    

    
