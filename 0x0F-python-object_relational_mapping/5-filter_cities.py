#!/usr/bin/python3

"""
    this script takes in the name of a state as an argument
    and lists all cities of that state, using the database hbtn_0e_4_usa
"""


if __name__ == '__main__':
    import sys
    import MySQLdb

    iter = 0

    host = 'localhost'
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    stateName = sys.argv[4]

    db = MySQLdb.connect(host=host, user=username, passwd=password,
                         db=database)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities, states WHERE \
    cities.state_id=states.id AND states.name=%s", ((stateName, )))
    result = cursor.fetchall()

    while (iter < len(result)):
        print(result[iter][0], end="")

        if (iter != (len(result) - 1)):
            print(', ', end="")
        else:
            print()

        iter += 1
