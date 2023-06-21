#!/usr/bin/python3

"""
    this module lists all the
    states from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':
    iter = 0
    import sys
    import MySQLdb
    import sqlalchemy

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute('SELECT id, name FROM states ORDER BY id')
    result = cursor.fetchall()

    while (iter < (len(result))):
        print(f"({result[iter][0]}, '{result[iter][1]}')")
        iter += 1
