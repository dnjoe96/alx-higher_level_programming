#!/usr/bin/python3
"""Script to select all states"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    dbInfo = sys.argv[1:]
    """
    db = MySQLdb.connect(host='localhost', user='root',\
             passwd='clearance', db='hbtn_0e_0_usa')
    """
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=dbInfo[0],
            passwd=dbInfo[1],
            db=dbInfo[2],
            charset='utf8'
            )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name\
            LIKE 'N%' ORDER BY id ASC;")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
