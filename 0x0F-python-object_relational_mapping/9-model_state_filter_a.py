#!/usr/bin/python3

"""
    this script lists all State objects that contain the
    letter a from the database hbtn_0e_6_usa
"""


if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    iter = 0

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id.asc()).all()

    while (iter < (len(result))):
        stateId = result[iter].id
        stateName = result[iter].name

        if 'a' in stateName:
            print("{}: {}".format(stateId, stateName))

        iter += 1
