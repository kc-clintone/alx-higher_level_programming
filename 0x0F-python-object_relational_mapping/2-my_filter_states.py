#!/usr/bin/python3
"""
A script that takes in an argument and displays all
values in the states where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Connect to the database and retrieve states
    """
    conn = db.connect(host="localhost", port=3306,
                    user=argv[1], passwd=argv[2], db=argv[3])
    csr = conn.cursor()
    csr.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
    states.id ASC".format(argv[4]))
    results = csr.fetchall()
    for item in results:
        print(item)
