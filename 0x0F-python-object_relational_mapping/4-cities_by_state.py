#!/usr/bin/python3
"""
this is a script to retrive imformation starting
from "N" in a database
"""


import sys
import MySQLdb


if __name__ == "__main__":
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=db_user,
                         passwd=db_password, database=db_database)

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities JOIN states ON cities.state_id = states.id;")

    rows = cursor.fetchall()

    for row in rows:
        print("{}".format(row))

    cursor.close()
    db.close()
