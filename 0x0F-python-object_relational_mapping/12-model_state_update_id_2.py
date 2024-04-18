#!/usr/bin/python3
"""
This is a script that changes the name of a State
object in the `hbtn_0e_6_usa` database
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Updates a State object in the database.
    """

    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    ngn = create_engine(database_url)
    sn = sessionmaker(bind=ngn)

    x = sn()

    res = x.query(State).filter(State.id == 2).first()
    res.name = "New Mexico"
    x.commit()
    x.close()
