#!/usr/bin/python3

"""
    this script adds the State object
    “Louisiana” to the database hbtn_0e_6_usa
"""


if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    stateName = 'Louisiana'

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name=stateName)
    session.add(new_state)
    session.commit()

    newStateId = session.query(State).filter_by(name=stateName)\
                                     .order_by(State.id.desc()).first()
    print(newStateId.id)
