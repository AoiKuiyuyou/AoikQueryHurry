# coding: utf-8
from __future__ import absolute_import

from aoikqueryhurry.db.sqlalchemy.rfunc_util import rfunc_tplt


#
def rfunc(info):
    #
    info.setdefault('driver', 'sqlite')
    info.setdefault('dbname', 'demo_db')
    info.setdefault('query', "SELECT 'hello'")

    #
    return rfunc_tplt(info, is_sqlite=True)

#
if __name__ == '__main__':
    rfunc(info={})
