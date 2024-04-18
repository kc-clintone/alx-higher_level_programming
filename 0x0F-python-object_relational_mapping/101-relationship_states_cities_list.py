#!/usr/bin/python3
"""
This script lists all State objects and City objects
 in the database
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
    Base.metadata.create_all(ngn)

    sn = sessionmaker(bind=ngn)
    x = sn()
    res = x.query(State).outerjoin(City).order_by(State.id, City.id).all()
    for i in res:
        print("{}: {}".format(i.id, i.name))
        for j in i.cities:
            print("    {}: {}".format(j.id, j.name))
