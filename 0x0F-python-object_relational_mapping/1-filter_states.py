#!/usr/bin/python3

"""
    Write a script that lists all states with a
    name starting with N (upper N) from supplied database
"""


if __name__ == '__main__':
    import sys
    import MySQLdb

    iter = 0

    host = 'localhost'
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host=host, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute('SELECT id, name FROM states ORDER BY id')
    result = cursor.fetchall()

    while (iter < (len(result))):
        if (result[iter][1][0] == 'N'):
            print(f"({result[iter][0]}, '{result[iter][1]}')")

        iter += 1
