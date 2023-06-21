#!/usr/bin/python3

"""
    this script lists all State objects
    from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    import sys
    import sqlalchemy
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    iter = 0

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format
                           (username, password, database))
    Session = sessionmaker(bind=engine)  # hold class returned by sessionmaker
    session = Session()  # make an instance of returned class

    result = session.query(State).order_by(State.id.asc()).all()

    while (iter < len(result)):
        stateId = result[iter].id
        stateName = result[iter].name

        print("{}: {}".format(stateId, stateName))
        iter += 1
