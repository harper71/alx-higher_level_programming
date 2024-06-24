#!/usr/bin/python3
"""
This script creates the State "California" with the City "San Francisco"
in the database hbtn_0e_100_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_database = sys.argv[3]

    # Create the engine to connect to the MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{db_user}:{db_password}@localhost/{db_database}',
        pool_pre_ping=True)

    # Create all tables in the database (if they don't exist)
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Check if "California" already exists
    california = session.query(State).filter_by(name='California').first()
    if not california:
        # Create new State object
        california = State(name='California')
        session.add(california)
        session.commit()

    # Create the City "San Francisco" linked to "California"
    san_francisco = City(name='San Francisco', state_id=california.id)
    session.add(san_francisco)
    session.commit()

    # Print the new City's id
    print(san_francisco.id)

    # Close the session
    session.close()
