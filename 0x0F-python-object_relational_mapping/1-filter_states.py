#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from the database
hbtn_0e_0_usa sorted in ascending order by states.id
"""
import MySQLdb
import sys


if __name__ == "__main__":

    user_name = sys.argv[1]
    user_password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user_name,
            passwd=user_password,
            db=database_name,
            charset="utf8"
        )
    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
