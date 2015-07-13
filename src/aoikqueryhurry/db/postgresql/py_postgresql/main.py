# coding: utf-8
from __future__ import absolute_import

from pprint import pformat

import postgresql.driver.dbapi20


#
def rfunc(info):
    #
    info.setdefault('host', '127.0.0.1')
    info.setdefault('port', 5432)
    info.setdefault('user', 'demo_user')
    info.setdefault('passwd', 'demo_pass')
    info.setdefault('dbname', 'demo_db')
    info.setdefault('query', "SELECT 'hello'")

    #
    conn_kwargs = dict(
        host=info['host'],
        port=int(info['port']),
        user=info['user'],
        password=info['passwd'],
        database=info['dbname'],
    )

    #
    print('# Connect')
    print(pformat(conn_kwargs, indent=4, width=1))

    #
    query = info['query']

    #
    print('# Query')
    print(query)

    #
    conn = None

    try:
        #
        conn = postgresql.driver.dbapi20.connect(**conn_kwargs)

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
            if not conn.closed:
                conn.close()

#
if __name__ == '__main__':
    rfunc(info={})
