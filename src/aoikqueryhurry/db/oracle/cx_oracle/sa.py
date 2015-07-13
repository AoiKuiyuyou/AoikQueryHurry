# coding: utf-8
from __future__ import absolute_import

from aoikqueryhurry.db.sqlalchemy.rfunc_util import rfunc_tplt


#
def rfunc(info):
    #
    info.setdefault('driver', 'oracle+cx_oracle')
    info.setdefault('host', '127.0.0.1')
    info.setdefault('port', 1521)
    info.setdefault('instance', 'XE')
    info.setdefault('user', 'demo_user')
    info.setdefault('passwd', 'demo_pass')
    info.setdefault('dbname', '')
    info.setdefault('query', """SELECT 'hello' FROM dual""")

    #
    return rfunc_tplt(info, is_oracle=True)
