#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_database = sys.argv[3]

    # Create the engine to connect to the MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{db_user}:{db_password}@localhost/{db_database}',
        pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all City objects and join with the State table
    results = session.query(City, State).join(State).order_by(City.id).all()

    # Print the results
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
