#!/usr/bin/python3
"""
This is a script that prints all City objects
from the `hbtn_0e_14_usa` database
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and retrieve the cities
    """

    conn = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    ngn = create_engine(conn)
    Base.metadata.create_all(ngn)
    sn = sessionmaker(bind=ngn)

    x = sn()
    st1 = State(name='California')
    ct1 = City(name='San Francisco')
    st1.cities.append(ct1)

    x.add(st1)
    x.commit()
    x.close()
