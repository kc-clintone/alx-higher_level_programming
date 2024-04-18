#!/usr/bin/python3
"""
This is a script that prints the first State object
from `hbtn_0e_6_usa` database.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and retrieve the state
    """

    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    ngn = create_engine(database_url)
    sn = sessionmaker(bind=ngn)

    x = sn()

    res = x.query(State).order_by(State.id).first()
    if res is not None:
        print('{0}: {1}'.format(res.id, res.name))
    else:
        print("Nothing")
