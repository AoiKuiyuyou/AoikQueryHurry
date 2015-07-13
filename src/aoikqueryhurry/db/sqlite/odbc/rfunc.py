# coding: utf-8
from __future__ import absolute_import

from aoikqueryhurry.db.odbc.rfunc_util import rfunc_tplt


#
def rfunc(info):
    #
    info.setdefault('odbc_dsn', '')
    info.setdefault('odbc_drvr', '')
    info.setdefault('dbname', 'demo_db')
    info.setdefault('query', "SELECT 'hello'")

    #
    return rfunc_tplt(info, is_sqlite=True)
