#!/usr/bin/python3
"""
this script lists all states from the database
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

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print("{}".format(row))

    cursor.close()
    db.close()
