#!/usr/bin/python3

"""
    this script takes in arguments and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument
    this also guards against SQL injection
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
    cursor.execute("SELECT * FROM states WHERE name='{}' ORDER BY ID".format(
        (stateName)))
    result = cursor.fetchall()

    while (iter < len(result)):
        print(f"({result[iter][0]}, '{result[iter][1]}')")
        iter += 1
