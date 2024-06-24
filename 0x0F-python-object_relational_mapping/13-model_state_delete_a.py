#!/usr/bin/python3
"""
Start link class to table in database
of mysql using sqlalcamey
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

    states_to_del = session1.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    for state in states_to_del:
        session1.delete(state)

    session1.commit()

    session1.close()
