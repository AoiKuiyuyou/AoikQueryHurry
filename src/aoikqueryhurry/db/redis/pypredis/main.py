# coding: utf-8
from __future__ import absolute_import

from pprint import pformat

from pypredis.client import EventLoop
from pypredis.client import TCPConnection


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
    eloop = None
    conn = None

    try:
        #
        conn = TCPConnection(**conn_kwargs)

        #
        eloop = EventLoop()
        eloop.start()

        #
        res = eloop.send_command(conn, 'info').result()

        #
        print('# Result')
        print(res)

    finally:
        #
        conn = None
        ## |conn| obj has no |close| method

        #
        if eloop is not None:
            eloop.stop()

#
if __name__ == '__main__':
    rfunc(info={})
