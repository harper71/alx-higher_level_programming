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

    states = session1.query(State).order_by(State.id).limit(1).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        if states is None:
            print("")

    session1.close()
