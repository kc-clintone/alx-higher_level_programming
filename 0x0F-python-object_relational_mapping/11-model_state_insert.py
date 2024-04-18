#!/usr/bin/python3
"""
This is a script that adds the State object
`Louisiana` to the `hbtn_0e_6_usa` database
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and retrieve state
    """

    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    ngn = create_engine(database_url)
    sn = sessionmaker(bind=ngn)

    x = sn()

    my_state = State(name="Louisiana")
    x.add(my_state)
    x.commit()

    print('{0}'.format(my_state.id))
    x.close()
