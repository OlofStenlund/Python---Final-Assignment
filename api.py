from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from seedfile import db

class Character(BaseModel):
    id: int = None
    name: str 
    description: str = None
    age: int = None
    home_planet: str = None

class Planet(BaseModel):
    id: int = None
    name: str
    sector: str = None

app = FastAPI()


#######################
# Simple get requests #
#######################


@app.get("/")
def root():
    return "Welcome"

@app.get("/planets/get_planets")
def get_planets():
    get_planets_query = """
    SELECT * FROM planets
    """
    planets = []
    res = db.call_db(get_planets_query)
    # Add results to list
    for i in res:
        id, name, sector= i
        planets.append(Planet(id=id, name=name, sector=sector))
    return planets

@app.get("/characters/get_characters")
def get_characters():
    get_character_query = """
    SELECT * FROM characters
    """
    characters = []
    res = db.call_db(get_character_query)
    for i in res:
        id, name, description, age, home_planet = i
        characters.append(Character(id=id, name=name, description= description, age= age, home_planet= home_planet))
    return characters


################################
# get requests with conditions #
################################


@app.get("/planets/get_planet_by_id/{id}")
def get_planet(id: int):
    get_planet_by_id_query = """
    SELECT * FROM planets WHERE id = ?
    """
    planets = []
    res = db.call_db(get_planet_by_id_query, id)
    for i in res:
        id, name, sector = i
        planets.append(Planet(id=id, name=name, sector=sector))
    return planets


@app.get("/characters/get_character_by_id/{id}")
def get_character(id: int):
    get_character_by_id_query = """
    SELECT * FROM characters WHERE id = ?
    """
    characters = []
    res = db.call_db(get_character_by_id_query, id)
    for i in res:
        id, name, description, age, home_planet = i
        characters.append(Character(id=id, name=name, description=description, age=age, home_planet=home_planet))
    return characters


@app.get("/planets/get_planet/{name}")
def get_planet(name: str):
    get_planet_by_name_query = """
    SELECT * FROM planets WHERE name = ?
    """
    # Put into list if there would be more than one result
    planets = []
    res = db.call_db(get_planet_by_name_query, name)
    for i in res:
        id, name, sector = i
        planets.append(Planet(id=id, name=name, sector=sector))
    return planets

@app.get("/characters/get_character/{name}")
def get_character(name: str):
    get_character_by_name_query = """
    SELECT * FROM characters WHERE name = ?
    """
    characters = []
    res = db.call_db(get_character_by_name_query, name)
    for i in res:
        id, name, description, age, home_planet = i
        characters.append(Character(id=id, name=name, description=description, age=age, home_planet=home_planet))
    return characters

@app.get("/character/get_character_by_planet/{planet}")
def get_character(planet: str):
    get_character_by_planet_query = """
    SELECT id, name, description, age FROM characters
    WHERE home_planet = ?
    """
    characters = []
    res = db.call_db(get_character_by_planet_query, planet)
    for i in res:
        id, name, description, age = i
        characters.append(Character(id=id, name=name, description=description, age=age))
    return characters

@app.get("/characters/get_oldest")
def get_character():
    get_oldest_character_query = """
    SELECT * FROM characters
    ORDER BY age DESC
    LIMIT 1
    """
    character = []
    res = db.call_db(get_oldest_character_query)
    for i in res:
        id, name, description, age, home_planet = i
        character.append(Character(id=id, name=name, description=description, age=age, home_planet=home_planet))
    return character

@app.get("/planets/get_by_sector/{sector}")
def get_planets(sector: str):
    select_planets_by_sector_query = """
    SELECT * FROM planets
    WHERE sector = ?
    """
    planets = []
    res = db.call_db(select_planets_by_sector_query, sector)
    for i in res:
        id, name, sector = i
        planets.append(Planet(id=id, name=name, sector=sector))
    return planets

@app.get("/planets/get_duplicates")
def get_planet_duplicates():
    # counting can be done in HAVING, no need for extra column
    get_planet_duplicates_query = """
    SELECT * FROM planets
    WHERE name IN (
        SELECT name
        FROM planets
        GROUP BY name
        HAVING COUNT(*) > 1
    )
    ORDER BY name
    """
    duplicates = []
    res = db.call_db(get_planet_duplicates_query)
    for i in res:
        id, name, sector = i
        duplicates.append(Planet(id=id, name=name, sector=sector))
    return duplicates

@app.get("/characters/get_duplicates")
def get_character_duplicates():
    get_character_duplicates_query = """
    SELECT * FROM characters
    WHERE name IN (
        SELECT name
        FROM characters
        GROUP BY name
        HAVING COUNT(*) > 1
    )
    ORDER BY name
    """
    duplicates = []
    res = db.call_db(get_character_duplicates_query)
    for i in res:
        id, name, description, age, home_planet = i
        duplicates.append(Character(id=id, name=name, description=description, age=age, home_planet=home_planet))
    return duplicates


#################
# Post requests #
#################


@app.post("/planets/add_planet")
def add_planet(planet: Planet):
    add_planet_query = """
    INSERT INTO planets (name, sector)
    VALUES (?, ?)
    """
    db.call_db(add_planet_query, planet.name, planet.sector)
    return "Planet added"

@app.post("/characters/add_character")
def add_character(character: Character):
    add_character_query = """
    INSERT INTO characters (name, description, age, home_planet)
    VALUES (?, ?, ?, ?)
    """
    db.call_db(add_character_query, character.name, character.description, character.age, character.home_planet)
    return "Character added"


################
# Put requests #
################


@app.put("/characters/modify_character/{id}")
def modify_character(id: int, new_character: Character):
    update_query = """
    UPDATE characters
    SET name = ?, description = ?, age = ?, home_planet = ?
    WHERE id = ?
    """
    # query, arguments in order. SET first, followed by name chosen
    db.call_db(update_query, new_character.name, new_character.description, new_character.age, new_character.home_planet, id)

@app.put("/planets/modify_planet/{id}")
def modify_planet(id: int, new_planet: Planet):
    update_query = """
    UPDATE planets
    SET name = ?, sector = ?
    WHERE id = ?
    """
    db.call_db(update_query, new_planet.name, new_planet.sector, id)

####################
# Delete requestes #
####################


@app.delete("/characters/delete_character/{id}")
def delete_character(id: int):
    delete_character_query = """
    DELETE FROM characters 
    WHERE id = ?
    """
    db.call_db(delete_character_query, id)
    return "Character deleted"

@app.delete("/planets/delete_planet/{id}")
def delete_character(id: int):
    delete_planet_query = """
    DELETE FROM planets 
    WHERE id = ?
    """
    db.call_db(delete_planet_query, id)
    return "Character deleted"

@app.delete("/planets/remove_duplicates")
def delete_duplicate_planets():    
    delete_query_planets = """
    DELETE FROM planets
    WHERE rowid NOT IN (
        SELECT MIN (rowid)
        FROM planets
        GROUP BY name, sector
        )
    """
    db.call_db(delete_query_planets)
    
@app.delete("/characters/remove_duplicates")
def delete_duplicate_characters():    
    delete_query_characters = """
    DELETE FROM characters
    WHERE rowid NOT IN (
        SELECT MIN (rowid)
        FROM characters
        GROUP BY name, description, home_planet, age
        )
    """
    db.call_db(delete_query_characters)

