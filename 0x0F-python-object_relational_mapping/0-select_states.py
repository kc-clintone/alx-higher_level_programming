#!/usr/bin/python3
"""
A script lists all states from the `hbtn_0e_0_usa` database
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Retrieve states from the database.
    """
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    dbcsr = db.cursor()
    dbcsr.execute("SELECT * FROM states")
    results = dbcsr.fetchall()
    for item in results:
        print(item)
