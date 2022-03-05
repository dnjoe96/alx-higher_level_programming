#!/usr/bin/python3
"""Script to select all states with a certain name to avoid SQL injection"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    dbInfo = sys.argv[1:]
    # db = MySQLdb.connect(host='localhost', user='root',\
    #         passwd='clearance', db='hbtn_0e_0_usa')
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=dbInfo[0],
            passwd=dbInfo[1],
            db=dbInfo[2],
            charset='utf8'
            )

    cur = db.cursor()
    cur.execute(
            "SELECT cities.id, cities.name, states.name\
            FROM cities\
            JOIN states ON state_id=states.id\
            WHERE states.name=%s\
            ORDER BY cities.id ASC;", (dbInfo[3], ))

    rows = cur.fetchall()
    allRows = []
    for row in rows:
        allRows.append(row[1])
    print(*allRows, sep=', ')

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
