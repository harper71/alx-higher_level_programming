#!/usr/bin/python3
"""Start link class to table in database
"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session_create = sessionmaker(bind=engine)

    session1 = session_create()

    state_search = sys.argv[4]

    states = session1.query(State).filter(
        State.name == state_search).order_by(State.id).first()

    if states:
        print(f"{states.id}")
    else:
        print("Not found")

    session1.close()
