# coding: utf-8
from __future__ import absolute_import

from pprint import pformat
import sqlite3


#
def rfunc(info):
    #
    info.setdefault('dbname', 'demo_db')
    info.setdefault('query', "SELECT 'hello'")

    #
    conn_args = [info['dbname']]

    #
    print('# Connect')
    print(pformat(conn_args, indent=4, width=1))

    #
    query = info['query']

    #
    print('# Query')
    print(query)

    #
    conn = None

    try:
        #
        conn = sqlite3.connect(*conn_args)

        cursor = conn.cursor()

        #
        cursor.execute(query)

        res = cursor.fetchall()

        #
        print('# Result')
        print(res)

    finally:
        #
        if conn is not None:
            conn.close()

#
if __name__ == '__main__':
    rfunc(info={})
