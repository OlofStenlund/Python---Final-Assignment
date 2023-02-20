
import sqlite3


class StarWarsDatabase:
    url: str

    def __init__(self, url: str, *args):
        self.url = url
        con = sqlite3.connect(url)
        cur = con.cursor()
        for table in args:
            con.execute(
                f"""
                CREATE DATABASE IF NOT EXISTS StarWars
                """)
        cur.close()
        con.commit()
        con.close()

    def call_db(self, query, *args):
        con = sqlite3.connect(self.url)
        cur = con.cursor()
        res = cur.execute(query, args)
        data = res.fetchall()
        cur.close()
        con.commit()
        con.close()
        return data
    
