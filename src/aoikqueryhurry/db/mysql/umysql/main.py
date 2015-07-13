# coding: utf-8
from __future__ import absolute_import

from pprint import pformat

import umysql


#
def rfunc(info):
    #
    info.setdefault('host', '127.0.0.1')
    info.setdefault('port', 3306)
    info.setdefault('user', 'demo_user')
    info.setdefault('passwd', 'demo_pass')
    info.setdefault('dbname', 'demo_db')
    info.setdefault('query', "SELECT 'hello'")

    #
    conn_args = [
        info['host'],
        int(info['port']),
        info['user'],
        info['passwd'],
        info['dbname'],
    ]

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
        conn = umysql.Connection()

        conn.connect(*conn_args)
        ## |umysql|'s connect args are defined here:
        ##  https://github.com/esnme/ultramysql/blob/f8703807c314e10188df7de97a53ace9c78943b7/python/umysql.c#L837

        #
        res_obj = conn.query(query)

        res = res_obj.rows[0][0]

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
