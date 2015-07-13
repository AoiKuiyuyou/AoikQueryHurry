# coding: utf-8
from __future__ import absolute_import

import cx_Oracle


#
def rfunc(info):
    #
    info.setdefault('host', '127.0.0.1')
    info.setdefault('port', 1521)
    info.setdefault('instance', 'XE')
    info.setdefault('user', 'demo_user')
    info.setdefault('passwd', 'demo_pass')
    info.setdefault('dbname', '')
    info.setdefault('query', """SELECT 'hello' FROM dual""")

    #
    host = info['host']

    port = int(info['port'])

    user = info['user']

    passwd = info['passwd']

    instance = info['instance']

    #
    conn_uri = '{user}{passwd}@{srvr}/{instance}'.format(
        user=user,
        passwd='/{}'.format(passwd) if passwd is not None else '',
        srvr='{}:{}'.format(host, port) if port is not None else host,
        instance='/{}'.format(instance) if instance else '',
    )

    #
    print('# Connect')
    print(conn_uri)

    #
    query = info['query']

    #
    print('# Query')
    print(query)

    #
    conn = None

    try:
        #
        conn = cx_Oracle.connect(conn_uri)

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
