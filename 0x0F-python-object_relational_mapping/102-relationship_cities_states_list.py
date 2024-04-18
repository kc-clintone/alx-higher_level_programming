#!/usr/bin/python3
"""
This script lists all City objects in the
hbtn_0e_101_usa database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    ngn = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    sn = sessionmaker(bind=ngn)
    x = sn()

    res = x.query(State).join(City).order_by(City.id).all()

    for i in res:
        for j in i.cities:
            print("{}: {} -> {}".format(j.id, j.name, i.name))
