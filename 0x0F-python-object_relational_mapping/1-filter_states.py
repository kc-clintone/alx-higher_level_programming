#!/usr/bin/python3
"""
A script lists all states with a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb as db
from sys import argv

"""
Establish connection to database and retrieve all states
"""

if __name__ == '__main__':
    sqldb = db.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])
    dbcsr = sqldb.cursor()
    dbcsr.execute(
    "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
    ORDER BY states.id ASC")
    results = dbcsr.fetchall()
    for item in results:
        print(item)
