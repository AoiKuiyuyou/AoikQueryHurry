# coding: utf-8
from __future__ import absolute_import

from pprint import pformat

from redis.client import StrictRedis


#
def rfunc(info):
    #
    info.setdefault('host', '127.0.0.1')
    info.setdefault('port', 6379)

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
        conn = StrictRedis(**conn_kwargs)

        #
        res = '\n'.join('{:<30}: {}'.format(k, v) for k, v in conn.info().items())

        #
        print('# Result')
        print(res)

    finally:
        #
        conn = None
        ## |conn| obj has no |close| method

#
if __name__ == '__main__':
    rfunc(info={})
