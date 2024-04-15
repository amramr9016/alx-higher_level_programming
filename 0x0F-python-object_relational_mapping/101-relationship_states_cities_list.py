#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects contained in the DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).outerjoin(City).order_by(State.id, City.id).all()

    for state_obj in states:
        print("{}: {}".format(state_obj.id_num, state_obj.state_name))
        for city_obj in state_obj.cities:
            print("    {}: {}".format(city_obj.id_num, city_obj.city_name))
