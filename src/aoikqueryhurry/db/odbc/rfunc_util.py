# coding: utf-8
from __future__ import absolute_import


#
def rfunc_tplt(info, is_freetds=False, is_oracle=False, is_sqlite=False):
    #
    info.setdefault('odbc_dsn', '')
    info.setdefault('odbc_drvr', '')
    info.setdefault('host', '')
    info.setdefault('port', '')
    info.setdefault('instance', '')
    info.setdefault('user', '')
    info.setdefault('passwd', '')
    info.setdefault('dbname', '')

    assert 'query' in info

    #
    conn_args = dict(
        dsn=info['odbc_dsn'],
        driver=info['odbc_drvr'],
        server=info['host'],
        port=info['port'],
        instance=info['instance'],
        database=info['dbname'],
        uid=info['user'],
        pwd=info['passwd'],
    )

    if is_sqlite:
        if info['odbc_dsn']:
            conn_uri = 'DSN={dsn};DATABASE={database};'.format(**conn_args)
        else:
            conn_uri = 'DRIVER={{{driver}}};DATABASE={database};'\
                .format(**conn_args)
    elif is_oracle:
        if info['odbc_dsn']:
            conn_uri = 'DSN={dsn};DATABASE={database};UID={uid};PWD={pwd};'\
                .format(**conn_args)
        else:
            conn_uri = (
                'DRIVER={{{driver}}};dbq={server}:{port}/{instance};'
                'DATABASE={database};UID={uid};PWD={pwd};'
            ).format(**conn_args)
    else:
        if info['odbc_dsn']:
            conn_uri = 'DSN={dsn};DATABASE={database};UID={uid};PWD={pwd};'\
                .format(**conn_args)
        else:
            conn_uri = (
                'DRIVER={{{driver}}};SERVER={server};PORT={port};'
                'DATABASE={database};UID={uid};PWD={pwd};'
            ).format(**conn_args)

        #
        if is_freetds:
            tds_version = info.get('tds_version', None)

            if tds_version is not None:
                conn_uri += 'TDS_VERSION={};'.format(tds_version)

    #
    cfunc = info['cfunc']

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
        conn = cfunc(conn_uri)

        cursor = conn.cursor()

        #
        cursor.execute(query)

        res = cursor.fetchall()

        cursor.close()

        #
        print('# Result')
        print(res)

    finally:
        #
        if conn is not None:
            conn.close()
