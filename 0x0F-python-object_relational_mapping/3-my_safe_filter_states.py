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

    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print("{}".format(row))

    cursor.close()
    db.close()
