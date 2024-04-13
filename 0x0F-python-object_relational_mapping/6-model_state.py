#!/usr/bin/python3
"""
A script that defines the state class
"""
import sys
from model_state import State, bse

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    ngin = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    bse.metadata.create_all(ngin)
