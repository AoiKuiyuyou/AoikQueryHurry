# coding: utf-8
from __future__ import absolute_import

from aoikqueryhurry.db.sqlalchemy.rfunc_util import rfunc_tplt


#
def rfunc(info):
    #
    info.setdefault('driver', 'mysql+oursql')
    info.setdefault('host', '127.0.0.1')
    info.setdefault('port', 3306)
    info.setdefault('user', 'demo_user')
    info.setdefault('passwd', 'demo_pass')
    info.setdefault('dbname', 'demo_db')
    info.setdefault('query', "SELECT 'hello'")

    #
    return rfunc_tplt(info)
