import json
from starwarsdatabase import StarWarsDatabase
import sqlite3

db = StarWarsDatabase("StarWars.db")

create_character_table = """
CREATE TABLE IF NOT EXISTS characters
(   id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    age INT,
    home_planet TEXT,
    FOREIGN KEY(home_planet) REFERENCES planets(name)
)
"""

create_planet_table = """
CREATE TABLE IF NOT EXISTS planets
(   id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    sector TEXT
)
"""

insert_character = """
INSERT INTO characters
(  
    name,
    description,
    age,
    home_planet
) 
VALUES 
(
    ?, ?, ?, ?
)
"""

insert_planet = """
INSERt INTO planets
(  
    name,
    sector
)
VALUES
(
?, ?
)
"""

while __name__ == "__main__":
    db.call_db(create_character_table)
    db.call_db(create_planet_table)

    with open("seed.json", "r") as seed:
        data = json.load(seed)

        for i in data["characters"]:
            print(i)
            db.call_db(insert_character, i["name"], i["description"], i["age"], i["home_planet"])

        for i in data["planets"]:
            print(i)
            db.call_db(insert_planet,  i["name"], i["sector"])
    break