## What to do

The database file creates the database and a method for calling the database.
The API defines the actions that can be taken. Acts as the mediator between the app and the datbase
The app/main defines the functions and the actual program to run
Maybe use a file for models, aka. object classes?

Try to scrape the 100 most popular books of 2020 from this page: https://www.stadsbiblioteket.nu/100-mest-utlanade-romanerna-2020/


IF YOU SPECIFY WHAT TYPE OF DATA YOU WANT IN, FASTAPI WILL AUTOMATICALLY CHECK FOR THE DATA TYPE.

1: Database: Creates the database using the right packages. 
    If using a SQL Server database, create a connection using pyodbc
    Create DB Class, no init needed?
    Method that creates the dartabase, and one  for calling kthe database
        Create: Method that connects, runs a create-query, and closes connection
        Call: Method that connects, and sends whatever query we want to run (from API)
    if __name__ == '__main__':
    db = DB()
    db.init_db()

2: API: The API defines the interactions that can take place between the app and the database.
    If the app wants to update a database, first create a function inside the app. The function uses the requests package
    to send a request to the right url(endpoint/route). 
    Check out details on why we need to use .json sometimes.
    from fastapi import FastAPI
    from requests import request
    from pydantic import BaseModel
    from typing import List

3: App: The app runs the program itself. Set functions to call the API, and then run the program to call the functions.
    Create a class for the object you want to insert into the database. In this file or other?
    Import requests and typings


4: Duplicates handling.
    Options: 1: How many duplicates in the tables?
        Return: Planets: 2 duplicates
                Characters: 0 duplicates
                Options: Remove all duplicates
                            See all duplicates
                            remove duplicates in one table only
                                Ooptions: Planets or characters

5: Add option to alter planet/character by ID



select *
count(*)
from planets
group by name