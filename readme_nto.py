# coding: utf-8
from functools import partial
import os.path
import sys

from aoikdyndocdsl.ext.all import nto as nto_dft
from aoikdyndocdsl.ext.markdown.heading import hd_to_key
from aoikdyndocdsl.ext.markdown.heading import hd_url
from aoikdyndocdsl.ext.var import var
from aoikdyndocdsl.ext.var import var_set
from aoikdyndocdsl.ext.var import var_set_v2
from aoikdyndocdsl.parser.ext import iarg_ctx
from aoikdyndocdsl.parser.ext import iarg_psr


#
_FILE_READER_CACHE = {}

_PREFIX_INFO_S = [
    # [uri_prefix, path_prefix]
    ('src/', './src/'),
    ('/var/Oracle/', None), # None means ignore, at 3xlIp4J
    ('/', './'),
]

def file_reader(key, val, file_path=None, line_num=None):
    #
    if file_path is not None:
        file_path_2 = file_path
    elif val.startswith('aoikqueryhurry.') or val.startswith('"aoikqueryhurry.'):
        # Module name to file path
        file_path_2 = val.strip('"').replace('.', '/')

        # Remove "function name" part
        file_path_2, sep, _ = file_path_2.partition('::')

        # Add path prefix and file extension
        file_path_2 = 'src/{}.py'.format(file_path_2)
    else:
        found = False

        for prefix_info in _PREFIX_INFO_S:
            uri_prefix = prefix_info[0]

            if val.startswith(uri_prefix):
                # 3xlIp4J
                path_prefix = prefix_info[1]

                if path_prefix is None:
                    found = False
                    break

                file_path_2 = val[len(uri_prefix):]

                if path_prefix:
                    file_path_2 = path_prefix + file_path_2

                found = True
                break

        if not found:
            msg = 'File checking ignores: {} {}\n'.format(key, val)
            sys.stderr.write(msg)
            return None, None

        assert file_path_2

    assert file_path_2

    #
    if line_num is None:
        if '#L' in file_path_2:
            file_path_2, sep, line_num = file_path_2.rpartition('#L')

            if not sep:
                line_num = None
            else:
                line_num = int(line_num)

    #
    file_path_2 = os.path.normpath(file_path_2)

    #
    txt = _FILE_READER_CACHE.get(file_path_2, None)

    if txt is None:
        file_obj = open(file_path_2)

        txt = file_obj.read()

        _FILE_READER_CACHE[file_path_2] = txt

    #
    return txt, line_num

#
v = var

vs = var_set

vs2 = partial(var_set_v2, file_reader=file_reader)

hk = hd_to_key

h = hd_url

#
def nto(name):
    obj = globals().get(name, None)

    if obj is None:
        obj = nto_dft(name)

    return obj
