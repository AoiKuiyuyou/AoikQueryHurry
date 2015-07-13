# coding: utf-8
from __future__ import absolute_import

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


try:
    from urllib.parse import quote_plus ## Py3
except ImportError:
    from urllib import quote_plus ## Py2


#
def rfunc_tplt(info, is_freetds=False, is_oracle=False, is_sqlite=False):
    #
    if is_sqlite:
        #
        engine_uri = '{driver}:///{dbname}'.format(
            driver=info['driver'],
            dbname=info['dbname'],
        )
    else:
        #
        driver = info['driver']

        host = info['host']

        port = info.get('port', None)

        user = info['user']

        passwd = info.get('passwd', None)

        dbname = info.get('dbname', None)

        instance = info.get('instance', None)

        #
        engine_uri = '{driver}://{user}{passwd}@{srvr}{instance}{dbname}'.format(
            driver=driver,
            user=user,
            passwd=':{}'.format(passwd) if passwd is not None else '',
            srvr='{}:{}'.format(host, port) if port is not None else host,
            instance='/{}'.format(instance) if instance else '',
            dbname='/{}'.format(dbname) if dbname else '',
        )

    #
    print('# Connect')
    print(engine_uri)

    #
    query = info['query']

    #
    print('# Query')
    print(query)

    #
    engine = None
    ssmkr = None
    session = None

    try:
        #
        engine = create_engine(engine_uri)

        #
        ssmkr = sessionmaker(
            bind=engine,
        )

        #
        session = ssmkr()

        #
        res_proxy = session.execute(query)

        res = res_proxy.fetchall()

        #
        print('# Result')
        print(res)

    finally:
        #
        if session is not None:
            session.close()

        ssmkr = None

        engine = None

def rfunc_tplt_odbc(info, is_freetds=False):
    #
    info.setdefault('odbc_dsn', '')
    info.setdefault('odbc_drvr', '')
    info.setdefault('host', '')
    info.setdefault('port', '')
    info.setdefault('user', '')
    info.setdefault('passwd', '')
    info.setdefault('dbname', '')

    assert 'driver' in info
    assert 'query' in info

    #
    conn_args = dict(
        dsn=info['odbc_dsn'],
        driver=info['odbc_drvr'],
        server=info['host'],
        port=info['port'],
        database=info['dbname'],
        uid='demo_user',
        pwd='demo_pass',
    )

    #
    if info['odbc_dsn']:
        odbc_uri = 'DSN={dsn};UID={uid};PWD={pwd};'.format(**conn_args)
    else:
        odbc_uri = (
            'DRIVER={{{driver}}};SERVER={server};PORT={port};'
            'DATABASE={database};UID={uid};PWD={pwd};'
        ).format(**conn_args)

    #
    if is_freetds:
        tds_version = info.get('tds_version', None)

        if tds_version is not None:
            odbc_uri += 'TDS_VERSION={};'.format(tds_version)

    #
    odbc_uri_esc = quote_plus(odbc_uri)

    #
    driver = info['driver']

    #
    engine_uri = '{driver}:///?odbc_connect={odbc_uri_esc}'.format(
        driver=driver,
        odbc_uri_esc=odbc_uri_esc,
    )

    #
    print('# Connect')
    print(engine_uri)

    #
    query = info['query']

    #
    engine = None
    ssmkr = None
    session = None

    try:
        #
        engine = create_engine(engine_uri)

        #
        ssmkr = sessionmaker(
            bind=engine,
        )

        #
        session = ssmkr()

        #
        res_proxy = session.execute(query)

        res = res_proxy.fetchall()

        #
        print('# Result')
        print(res)

    finally:
        #
        if session is not None:
            session.close()

        ssmkr = None

        engine = None
