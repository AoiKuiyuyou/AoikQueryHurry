# coding: utf-8
from __future__ import absolute_import

from pprint import pformat

from pymongo import MongoClient


#
def rfunc(info):
    #
    info.setdefault('host', '127.0.0.1')
    info.setdefault('port', 27017)

    #
    conn_kwargs = dict(
        host=info['host'],
        port=int(info['port']),
    )

    #
    print('# Connect')
    print(pformat(conn_kwargs, indent=4, width=1))

    #
    conn = None

    try:
        #
        conn = MongoClient(**conn_kwargs)

        #
        res = conn.testdb.col.find({})

        print('# Result')
        print(res)

    finally:
        #
        if conn is not None:
            conn.close()

#
if __name__ == '__main__':
    rfunc(info={})
