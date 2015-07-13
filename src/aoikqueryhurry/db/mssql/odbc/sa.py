# coding: utf-8
from __future__ import absolute_import

import sys

from aoikqueryhurry.db.sqlalchemy.rfunc_util import rfunc_tplt_odbc


#
def rfunc(info):
    #
    info.setdefault('driver', 'mssql+pyodbc')
    info.setdefault('odbc_dsn', '')
    info.setdefault('odbc_drvr', '')
    info.setdefault('host', '127.0.0.1')
    info.setdefault('port', 1433)
    info.setdefault('dbname', 'demo_db')
    info.setdefault('user', 'demo_user')
    info.setdefault('passwd', 'demo_pass')
    info.setdefault('query', "SELECT 'hello'")

    #
    is_freetds = sys.platform.startswith('linux')

    if is_freetds:
        info.setdefault('tds_version', '8.0')

    return rfunc_tplt_odbc(info, is_freetds=is_freetds)
