# coding: utf-8
from __future__ import absolute_import

import sys

from aoikargutil import ensure_spec
from aoikexcutil import get_traceback_stxt
from aoikimportutil import load_obj_local_or_remote
from aoikqueryhurry.main.argpsr import parser_make
from aoikqueryhurry.main.argpsr_const import ARG_CFUNC_URI_K
from aoikqueryhurry.main.argpsr_const import ARG_DBNAME_K
from aoikqueryhurry.main.argpsr_const import ARG_DEBUG_BOOL_K
from aoikqueryhurry.main.argpsr_const import ARG_DRVR_K
from aoikqueryhurry.main.argpsr_const import ARG_HOST_K
from aoikqueryhurry.main.argpsr_const import ARG_INSTANCE_K
from aoikqueryhurry.main.argpsr_const import ARG_ODBC_DRVR_K
from aoikqueryhurry.main.argpsr_const import ARG_ODBC_DSN_K
from aoikqueryhurry.main.argpsr_const import ARG_PASSWD_K
from aoikqueryhurry.main.argpsr_const import ARG_PORT_K
from aoikqueryhurry.main.argpsr_const import ARG_QUERY_K
from aoikqueryhurry.main.argpsr_const import ARG_RFUNC_URI_K
from aoikqueryhurry.main.argpsr_const import ARG_SPEC
from aoikqueryhurry.main.argpsr_const import ARG_USER_K
from aoikqueryhurry.main.argpsr_const import ARG_VER_BOOL_K
from aoikqueryhurry.main.main_const import CFUNC_DYN_MOD_NAME
from aoikqueryhurry.main.main_const import MAIN_RET_V_CFUNC_LOAD_ER
from aoikqueryhurry.main.main_const import MAIN_RET_V_EXC_LEAK_ER
from aoikqueryhurry.main.main_const import MAIN_RET_V_KBINT_OK
from aoikqueryhurry.main.main_const import MAIN_RET_V_RFUNC_LOAD_ER
from aoikqueryhurry.main.main_const import MAIN_RET_V_RFUNC_RUN_ER
from aoikqueryhurry.main.main_const import MAIN_RET_V_RFUNC_RUN_OK
from aoikqueryhurry.main.main_const import MAIN_RET_V_VER_SHOW_OK
from aoikqueryhurry.main.main_const import RFUNC_DYN_MOD_NAME
from aoikqueryhurry.version import VERSION


#
def main_imp():
    #
    parser = parser_make()

    args_obj = parser.parse_args()

    #
    ensure_spec(parser, ARG_SPEC)

    #
    ver_bool = getattr(args_obj, ARG_VER_BOOL_K)

    #
    if ver_bool:
        #/
        print(VERSION)

        #/
        return MAIN_RET_V_VER_SHOW_OK

    #
    debug_bool = getattr(args_obj, ARG_DEBUG_BOOL_K)

    #
    cfunc_uri = getattr(args_obj, ARG_CFUNC_URI_K)

    #
    if cfunc_uri is None:
        cfunc = None
    else:
        try:
            cfunc = load_obj_local_or_remote(cfunc_uri,
                mod_name=CFUNC_DYN_MOD_NAME,
            )
        except Exception:
            #
            msg = '# Error\nFailed loading connect function.\nURI is |{}|.\n'.format(cfunc_uri)

            #
            sys.stderr.write(msg)

            #
            if debug_bool:
                tb_msg = get_traceback_stxt()

                sys.stderr.write('---\n{}---\n'.format(tb_msg))

            #
            return MAIN_RET_V_CFUNC_LOAD_ER

    #
    rfunc_uri = getattr(args_obj, ARG_RFUNC_URI_K)

    #
    try:
        rfunc = load_obj_local_or_remote(rfunc_uri,
            mod_name=RFUNC_DYN_MOD_NAME,
        )
    except Exception:
        #
        msg = '# Error\nFailed loading runner function.\nURI is |{}|.\n'.format(rfunc_uri)

        #
        sys.stderr.write(msg)

        #
        if debug_bool:
            tb_msg = get_traceback_stxt()

            sys.stderr.write('---\n{}---\n'.format(tb_msg))

        #
        return MAIN_RET_V_RFUNC_LOAD_ER

    #
    rfunc_info = {
        'driver': getattr(args_obj, ARG_DRVR_K),
        'odbc_drvr': getattr(args_obj, ARG_ODBC_DRVR_K),
        'odbc_dsn': getattr(args_obj, ARG_ODBC_DSN_K),
        'host': getattr(args_obj, ARG_HOST_K),
        'port': getattr(args_obj, ARG_PORT_K),
        'instance': getattr(args_obj, ARG_INSTANCE_K),
        'user': getattr(args_obj, ARG_USER_K),
        'passwd': getattr(args_obj, ARG_PASSWD_K),
        'dbname': getattr(args_obj, ARG_DBNAME_K),
        'query': getattr(args_obj, ARG_QUERY_K),
        'cfunc': cfunc,
    }

    # Remove items with None value
    rfunc_info = dict(x for x in rfunc_info.items() if x[1] is not None)

    #
    try:
        rfunc(rfunc_info)
    except Exception:
        #
        msg = '# Error\nFailed running runner function.\nURI is |{}|.\n'.format(rfunc_uri)

        sys.stderr.write(msg)

        #
        if debug_bool:
            tb_msg = get_traceback_stxt()

            sys.stderr.write('---\n{}---\n'.format(tb_msg))

        #
        return MAIN_RET_V_RFUNC_RUN_ER

    #
    return MAIN_RET_V_RFUNC_RUN_OK

#
def main():
    #
    try:
        #
        return main_imp()
    #
    except KeyboardInterrupt:
        #
        return MAIN_RET_V_KBINT_OK
    #
    except Exception:
        #
        tb_msg = get_traceback_stxt()

        sys.stderr.write('# Uncaught exception\n---\n{}---\n'.format(tb_msg))

        #
        return MAIN_RET_V_EXC_LEAK_ER
