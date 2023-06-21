#!/usr/bin/python3

"""
    this script prints all City objects
    from the database hbtn_0e_14_usa
"""


if __name__ == '__main__':
    import sys
    from model_city import City
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

    result = session.query(State, City).join(City, State.id == City.state_id)\
                                       .all()

    while (iter < len(result)):
        stateName = result[iter][0].name
        cityId = result[iter][1].id
        cityName = result[iter][1].name

        print(f"{stateName}: ({cityId}) {cityName}")
        iter += 1
