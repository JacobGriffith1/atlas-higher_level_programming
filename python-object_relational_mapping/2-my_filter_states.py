#!/usr/bin/python3
"""
Script takes in an argument and displays all values
in the [states] table of [hbtn_0e_0_usa] where [name]
matches the argument
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    csr = db.cursor()
    csr.execute("SELECT * \
                 FROM `states` \
                 WHERE BINARY `name` = '{}' \
                 ORDER BY `id`".format(sys.argv[4]))
    state = csr.fetchall()

    for state in state:
        print(state)
