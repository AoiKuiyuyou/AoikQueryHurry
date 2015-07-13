# coding: utf-8
from __future__ import absolute_import

from aoikargutil import SPEC_DI_K_ONE


#
ARG_HELP_BOOL_F = '-h'
ARG_HELP_BOOL_F2 = '--help'

#
ARG_RFUNC_URI_F = '-R'
ARG_RFUNC_URI_K = '6xyYT1x'
ARG_RFUNC_URI_V = 'RFUNC_URI'
ARG_RFUNC_URI_H = 'Runner function.'

#
ARG_CFUNC_URI_F = '-C'
ARG_CFUNC_URI_K = '9pvy1a3'
ARG_CFUNC_URI_V = 'CFUNC_URI'
ARG_CFUNC_URI_H = 'Connect function.'

#
ARG_DRVR_F = '-D'
ARG_DRVR_K = '9qdrDDN'
ARG_DRVR_V = 'SA_DRVR'
ARG_DRVR_H = 'SQLAlchemy driver.'

#
ARG_ODBC_DRVR_F = '-O'
ARG_ODBC_DRVR_K = '6wVOXQ2'
ARG_ODBC_DRVR_V = 'ODBC_DRVR'
ARG_ODBC_DRVR_H = 'ODBC driver.'

#
ARG_ODBC_DSN_F = '-S'
ARG_ODBC_DSN_K = '4gGFMQu'
ARG_ODBC_DSN_V = 'ODBC_DSN'
ARG_ODBC_DSN_H = 'ODBC DSN.'

#
ARG_HOST_F = '-H'
ARG_HOST_K = '4htqQo3'
ARG_HOST_V = 'HOST'
ARG_HOST_H = 'Database host.'

#
ARG_PORT_F = '-P'
ARG_PORT_K = '8gLKP5c'
ARG_PORT_V = 'PORT'
ARG_PORT_H = 'Database port.'

#
ARG_INSTANCE_F = '-I'
ARG_INSTANCE_K = '9faTLQp'
ARG_INSTANCE_V = 'INSTANCE'
ARG_INSTANCE_H = 'Database instance.'

#
ARG_USER_F = '-u'
ARG_USER_K = '4jYy8nz'
ARG_USER_V = 'USER'
ARG_USER_H = 'Database user.'

#
ARG_PASSWD_F = '-p'
ARG_PASSWD_K = '6gyNscz'
ARG_PASSWD_V = 'PASSWD'
ARG_PASSWD_H = 'Database password.'

#
ARG_DBNAME_F = '-d'
ARG_DBNAME_K = '3dMrLwy'
ARG_DBNAME_V = 'DBNAME'
ARG_DBNAME_H = 'Database name.'

#
ARG_QUERY_F = '-q'
ARG_QUERY_K = '7e9Bwnl'
ARG_QUERY_V = 'QUERY'
ARG_QUERY_H = 'Query.'

#/
ARG_VER_BOOL_F = '-v'
ARG_VER_BOOL_K = '8dMyhVL'
ARG_VER_BOOL_A = 'store_true'
ARG_VER_BOOL_H = 'Show version.'

#
ARG_DEBUG_BOOL_F = '-V'
ARG_DEBUG_BOOL_K = '5uxy8gX'
ARG_DEBUG_BOOL_D = True
ARG_DEBUG_BOOL_V = '1|0'
ARG_DEBUG_BOOL_H = """Debug messages on/off. Default is {}."""\
    .format('on' if ARG_DEBUG_BOOL_D else 'off')

#
ARG_SPEC = {
    SPEC_DI_K_ONE: (
        ARG_HELP_BOOL_F,
        ARG_HELP_BOOL_F2,
        ARG_VER_BOOL_F,
        ARG_RFUNC_URI_F,
    )
}
