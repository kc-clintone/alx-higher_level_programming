#!/usr/bin/python3
"""
This is a script that prints all City objects
from the `hbtn_0e_14_usa` database
"""

from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and retrieve the cities
    """

    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    ngn = create_engine(database_url)
    sn = sessionmaker(bind=ngn)
    x = sn()

    res = x.query(City, State).join(State)

    for i, j in res.all():
        print("{}: ({}) {}".format(j.name, i.id, i.name))

    x.commit()
    x.close()
