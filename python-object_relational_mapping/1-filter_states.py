#!/usr/bin/python3
"""
Script lists all [states] with a [name] starting with [N]
from database [hbtn_0e_0_usa]
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
                 WHERE `name` \
                 LIKE BINARY 'N%' \
                 ORDER BY `id`")
    states = csr.fetchall()

    for state in states:
        print(state)
