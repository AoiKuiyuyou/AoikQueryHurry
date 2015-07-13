# coding: utf-8
from __future__ import absolute_import

from argparse import ArgumentParser

from aoikargutil import bool_0or1
from aoikqueryhurry.main.argpsr_const import ARG_CFUNC_URI_F
from aoikqueryhurry.main.argpsr_const import ARG_CFUNC_URI_H
from aoikqueryhurry.main.argpsr_const import ARG_CFUNC_URI_K
from aoikqueryhurry.main.argpsr_const import ARG_CFUNC_URI_V
from aoikqueryhurry.main.argpsr_const import ARG_DBNAME_F
from aoikqueryhurry.main.argpsr_const import ARG_DBNAME_H
from aoikqueryhurry.main.argpsr_const import ARG_DBNAME_K
from aoikqueryhurry.main.argpsr_const import ARG_DBNAME_V
from aoikqueryhurry.main.argpsr_const import ARG_DEBUG_BOOL_D
from aoikqueryhurry.main.argpsr_const import ARG_DEBUG_BOOL_F
from aoikqueryhurry.main.argpsr_const import ARG_DEBUG_BOOL_H
from aoikqueryhurry.main.argpsr_const import ARG_DEBUG_BOOL_K
from aoikqueryhurry.main.argpsr_const import ARG_DEBUG_BOOL_V
from aoikqueryhurry.main.argpsr_const import ARG_DRVR_F
from aoikqueryhurry.main.argpsr_const import ARG_DRVR_H
from aoikqueryhurry.main.argpsr_const import ARG_DRVR_K
from aoikqueryhurry.main.argpsr_const import ARG_DRVR_V
from aoikqueryhurry.main.argpsr_const import ARG_HOST_F
from aoikqueryhurry.main.argpsr_const import ARG_HOST_H
from aoikqueryhurry.main.argpsr_const import ARG_HOST_K
from aoikqueryhurry.main.argpsr_const import ARG_HOST_V
from aoikqueryhurry.main.argpsr_const import ARG_INSTANCE_F
from aoikqueryhurry.main.argpsr_const import ARG_INSTANCE_H
from aoikqueryhurry.main.argpsr_const import ARG_INSTANCE_K
from aoikqueryhurry.main.argpsr_const import ARG_INSTANCE_V
from aoikqueryhurry.main.argpsr_const import ARG_ODBC_DRVR_F
from aoikqueryhurry.main.argpsr_const import ARG_ODBC_DRVR_H
from aoikqueryhurry.main.argpsr_const import ARG_ODBC_DRVR_K
from aoikqueryhurry.main.argpsr_const import ARG_ODBC_DRVR_V
from aoikqueryhurry.main.argpsr_const import ARG_ODBC_DSN_F
from aoikqueryhurry.main.argpsr_const import ARG_ODBC_DSN_H
from aoikqueryhurry.main.argpsr_const import ARG_ODBC_DSN_K
from aoikqueryhurry.main.argpsr_const import ARG_ODBC_DSN_V
from aoikqueryhurry.main.argpsr_const import ARG_PASSWD_F
from aoikqueryhurry.main.argpsr_const import ARG_PASSWD_H
from aoikqueryhurry.main.argpsr_const import ARG_PASSWD_K
from aoikqueryhurry.main.argpsr_const import ARG_PASSWD_V
from aoikqueryhurry.main.argpsr_const import ARG_PORT_F
from aoikqueryhurry.main.argpsr_const import ARG_PORT_H
from aoikqueryhurry.main.argpsr_const import ARG_PORT_K
from aoikqueryhurry.main.argpsr_const import ARG_PORT_V
from aoikqueryhurry.main.argpsr_const import ARG_QUERY_F
from aoikqueryhurry.main.argpsr_const import ARG_QUERY_H
from aoikqueryhurry.main.argpsr_const import ARG_QUERY_K
from aoikqueryhurry.main.argpsr_const import ARG_QUERY_V
from aoikqueryhurry.main.argpsr_const import ARG_RFUNC_URI_F
from aoikqueryhurry.main.argpsr_const import ARG_RFUNC_URI_H
from aoikqueryhurry.main.argpsr_const import ARG_RFUNC_URI_K
from aoikqueryhurry.main.argpsr_const import ARG_RFUNC_URI_V
from aoikqueryhurry.main.argpsr_const import ARG_USER_F
from aoikqueryhurry.main.argpsr_const import ARG_USER_H
from aoikqueryhurry.main.argpsr_const import ARG_USER_K
from aoikqueryhurry.main.argpsr_const import ARG_USER_V
from aoikqueryhurry.main.argpsr_const import ARG_VER_BOOL_A
from aoikqueryhurry.main.argpsr_const import ARG_VER_BOOL_F
from aoikqueryhurry.main.argpsr_const import ARG_VER_BOOL_H
from aoikqueryhurry.main.argpsr_const import ARG_VER_BOOL_K


#
def parser_make():
    #
    parser = ArgumentParser(add_help=True)

    #
    parser.add_argument(
        ARG_RFUNC_URI_F,
        dest=ARG_RFUNC_URI_K,
        metavar=ARG_RFUNC_URI_V,
        help=ARG_RFUNC_URI_H,
    )

    parser.add_argument(
        ARG_CFUNC_URI_F,
        dest=ARG_CFUNC_URI_K,
        metavar=ARG_CFUNC_URI_V,
        help=ARG_CFUNC_URI_H,
    )

    parser.add_argument(
        ARG_DRVR_F,
        dest=ARG_DRVR_K,
        metavar=ARG_DRVR_V,
        help=ARG_DRVR_H,
    )

    parser.add_argument(
        ARG_ODBC_DRVR_F,
        dest=ARG_ODBC_DRVR_K,
        metavar=ARG_ODBC_DRVR_V,
        help=ARG_ODBC_DRVR_H,
    )

    parser.add_argument(
        ARG_ODBC_DSN_F,
        dest=ARG_ODBC_DSN_K,
        metavar=ARG_ODBC_DSN_V,
        help=ARG_ODBC_DSN_H,
    )

    parser.add_argument(
        ARG_HOST_F,
        dest=ARG_HOST_K,
        metavar=ARG_HOST_V,
        help=ARG_HOST_H,
    )

    parser.add_argument(
        ARG_PORT_F,
        dest=ARG_PORT_K,
        metavar=ARG_PORT_V,
        help=ARG_PORT_H,
    )

    parser.add_argument(
        ARG_INSTANCE_F,
        dest=ARG_INSTANCE_K,
        metavar=ARG_INSTANCE_V,
        help=ARG_INSTANCE_H,
    )

    parser.add_argument(
        ARG_USER_F,
        dest=ARG_USER_K,
        metavar=ARG_USER_V,
        help=ARG_USER_H,
    )

    parser.add_argument(
        ARG_PASSWD_F,
        dest=ARG_PASSWD_K,
        metavar=ARG_PASSWD_V,
        help=ARG_PASSWD_H,
    )

    parser.add_argument(
        ARG_DBNAME_F,
        dest=ARG_DBNAME_K,
        metavar=ARG_DBNAME_V,
        help=ARG_DBNAME_H,
    )

    parser.add_argument(
        ARG_QUERY_F,
        dest=ARG_QUERY_K,
        metavar=ARG_QUERY_V,
        help=ARG_QUERY_H,
    )

    parser.add_argument(
        ARG_VER_BOOL_F,
        dest=ARG_VER_BOOL_K,
        action=ARG_VER_BOOL_A,
        help=ARG_VER_BOOL_H,
    )

    parser.add_argument(
        ARG_DEBUG_BOOL_F,
        dest=ARG_DEBUG_BOOL_K,
        type=bool_0or1,
        nargs='?',
        const=True,
        default=ARG_DEBUG_BOOL_D,
        metavar=ARG_DEBUG_BOOL_V,
        help=ARG_DEBUG_BOOL_H,
    )

    #
    return parser
