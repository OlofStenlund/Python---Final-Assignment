from functions import add_character, get_character_by_name, get_character_by_planet
from api import Character


def print_me():
    print("Mememe")

def something_else(func, me):
    func()
    print(f"Something else, like {me}")

something_else(print_me, "you")



def alter_character_second(character, x, thing_to_mod, thing_to_print):
    if len(character) > 1:
        os.system('cls')
        print("There is more than one {x} with that name.")
        thing_to_print(character)
        id = input("Type the ID of the {x} you'd like to alter: ")
        thing_to_mod(id)
        input("")
    elif len(character) == 1:
        id = character[0]['id']
        thing_to_mod(id)
        input("")
    else: 
        print("Invalid entry")
        input("")
        return  