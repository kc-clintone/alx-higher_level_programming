#!/usr/bin/python3
"""
This script lists all State objects from the
database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Accessed the database and get the states
    """

    dburl = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    ngin = create_engine(dburl)
    sn = sessionmaker(bind=ngin)

    k = sn()

    for i in k.query(State).order_by(State.id):
        print('{0}: {1}'.format(i.id, i.name))
