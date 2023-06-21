#!/usr/bin/python3

"""
    this script lists all cities
    from the database hbtn_0e_4_usa
"""


if __name__ == '__main__':
    import sys
    import MySQLdb

    iter = 0

    host = 'localhost'
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host=host, user=username, passwd=password,
                         db=database)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities, \
    states WHERE cities.state_id=states.id ORDER BY cities.id")
    result = cursor.fetchall()

    while (iter < len(result)):
        print(f"({result[iter][0]}, '{result[iter][1]}', '{result[iter][2]}')")
        iter += 1
