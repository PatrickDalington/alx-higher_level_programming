#!/usr/bin/python3

"""
    this script prints the first State
    object from the database hbtn_0e_6_usa
"""


if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id.asc()).first()

    if result:
        stateId = result.id
        stateName = result.name

        print("{}: {}".format(stateId, stateName))
    else:
        print("Nothing")
