from functions import *
import os



def url(route: str):
    return f"http://127.0.0.1:8000{route}"

def print_menu():
    print("Hello there! Welcome to the Imperial Database.")
    print("Here are your options:")
    print("""1: See list of planets. 
2: See list of people.
3: Alter people/creatures.
4: Alter planets.
5: Detailed query regarding people/creatures.
6: Detailed query regarding plantes.
7: Handle duplicates
8: Exit.

""")



def main():  
    while True:
        os.system('cls')
        while True:
            print_menu()
            first_choice = input("Please enter your choice: ").strip()
            check = check_input(first_choice, 1, 9)
            if check == False:
                os.system('cls')
                input("Not valid entry. Choose again.")
                os.system('cls')
                pass
            else:
                break

        match int(first_choice):    
            case 1:
                os.system('cls')
                print("Planets:")
                ret = get_planets()
                print_planet(ret)
                input("Press any key to go back to main menu.")
            case 2: 
                os.system('cls')
                ret = get_characters()
                print("People and creatures:")
                print_person(ret)
                input("Press any key to go back to main menu.")          
            case 3:
                os.system('cls')
                while True:
                    print("1: Add person/creature. \n2: Modify person/creature. \n3: Delete person/creature \n4: Go back")
                    second_choice = input("Choose action: ").strip()
                    check = check_input(second_choice, 1, 5)
                    if check == False:
                        pass
                    else:
                        break

                second_choice = int(second_choice)          
                if second_choice == 1:
                    os.system('cls')
                    print("Adding person/creature: ")
                    add_character()
                    input("Creature added.")
                    continue
                elif second_choice == 2:
                    os.system('cls')
                    print("Modifying person/creature: ")
                    if modify_character(get_characters()) == True:
                        input("Modofication complete.")
                    continue
                elif second_choice == 3:
                    os.system('cls')
                    print("Deleting person/creature: ")
                    delete_character(get_characters())
                    input("Creature deleted.")
                    continue
                elif second_choice == 4:
                    continue
                else:
                    continue
            case 4:
                os.system('cls')
                while True:
                    print("What action would you like to take?")
                    print("1: Add planet. \n2: Update planet. \n3: Delete planet. \n4: Go back")
                    second_choice = input("Choose an action: ").strip()
                    check = check_input(second_choice, 1, 5)
                    if check == False:
                        pass
                    else:
                        break
            
                second_choice = int(second_choice)          
                if second_choice == 1:
                    os.system('cls')
                    print("Adding planet: ")
                    add_planet()
                    input("Planet added.")
                    continue
                elif second_choice == 2:
                    os.system('cls')
                    print("Modifying planet: ")
                    if modify_planet(get_planets()) == True:
                        input("Modifaction complete.")
                    continue
                elif second_choice == 3:
                    os.system('cls')
                    print("Deleting planet: ")
                    delete_planet(get_planets())
                    input("Planet deleted.")
                    continue
                elif second_choice == 4:
                    continue
            case 5:
                while True:
                    os.system('cls')
                    print("1: Select individual. \n2: Show oldest individual \n3: Show individuals from a certain planet \n4: Go back")
                    second_choice = input("Choose action: ").strip()
                    check = check_input(second_choice, 1, 5)
                    if check == False:
                        print("Invalid input.")
                        input("")
                        pass
                    else:
                        break

                second_choice = int(second_choice)
                if second_choice == 1:
                    os.system('cls')
                    print("What is the name of this induvidual?")
                    char = input("")
                    os.system('cls')
                    ret = get_character_by_name(char)
                    print_person(ret)
                    input("Press any key to go back to main menu.")
                    continue
                if second_choice == 2:
                    ret = get_oldest_character()
                    os.system('cls')
                    print("Oldest inividual in the dataset:")
                    print_person(ret)
                    input("Press any key to go back to main menu.")
                    continue
                if second_choice == 3:
                    os.system('cls')
                    print("What is the name of the planet?")
                    planet = input("")
                    ret = get_character_by_planet(planet)
                    os.system('cls')
                    print(f"Individuals from the planet of {planet}")
                    for i in ret:
                        print(f"Name: {i['name']} | Description: {i['description']} | Age: {i['age']}")
                    input("Press any key to go back to main menu.")
                    continue
                if second_choice == 4:
                    continue
                break
            case 6:
                while True:
                    os.system('cls')
                    print("1: Select planet. \n2: Show planets from a certain sector \n3: Go back")
                    second_choice = input("Choose action: ").strip()
                    check = check_input(second_choice, 1, 4)
                    if check == False:
                        print("Invalid input.")
                        input("")
                        pass
                    else:
                        break

                second_choice = int(second_choice)
                if second_choice == 1:
                    os.system('cls')
                    print("What is the name of the planet")
                    planet = input("")
                    os.system('cls')
                    ret = get_planet_by_name(planet)
                    print_planet(ret)
                    input("Press any key to go back to main menu.")
                    continue
                if second_choice == 2:
                    os.system('cls')
                    print("What is the name of the sector")
                    sector = input("")
                    ret = get_planets_by_sector(sector)
                    os.system('cls')
                    print(f"Planets from sector {sector}")
                    print_planet(ret)
                    input("Press any key to go back to main menu.")
                    continue
                if second_choice ==3:
                    continue
            case 7:
                os.system('cls')
                plan_dup = get_planet_duplicates()
                char_dup = get_character_duplicates()
                print(f"There are {len(plan_dup)} planets with the same name")
                print_planet(plan_dup)
                print(f"There are {len(char_dup)} indivicuals with the same name")
                print_person(char_dup)
                while True:
                    print("\nOptions:")
                    print("1: Delete exakt duplicates in both tables. \n2: Delete exact duplicates in Planets. \n3: Delete exact duplicates in Individuals  \n4: Go back")
                    second_choice = input("Choose action: ").strip()
                    check = check_input(second_choice, 1, 5)
                    if check == False:
                        print("Invalid input.")
                        input("")
                        pass
                    else:
                        break
                second_choice = int(second_choice)
                if second_choice == 1: 
                    remove_duplicate_planets()
                    remove_duplicate_characters()
                elif second_choice == 2:
                    remove_duplicate_planets()
                elif second_choice == 3:
                    remove_duplicate_characters()
                elif second_choice == 4:
                    continue
                print("Duplicates removed.")
                input("Press any key to go go back to main menu")
                continue

            case 8:
                inp = input("Exiting. Please confirm ('y')").strip().upper()
                if inp == "Y":
                    exit()
                else:
                    pass
            case other:
                os.system('cls')
                print("Invalid input. Try again")
                input("")
                

main()
