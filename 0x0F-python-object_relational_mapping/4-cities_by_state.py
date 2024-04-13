#!/usr/bin/python3
"""
This script lists all cities from the database
`hbtn_0e_4_usa`
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Connect to the database and retrieve cities
    """

    conn = db.connect(host="localhost", port=3306,
           user=argv[1], passwd=argv[2], db=argv[3])
    with conn.cursor() as csr:
        csr.execute(
"SELECT cities.id, cities.name, states.name \
FROM cities JOIN states ON cities.state_id \
= states.id ORDER BY cities.id ASC")
        res = csr.fetchall()
    if res is not None:
        for item in res:
            print(item)
