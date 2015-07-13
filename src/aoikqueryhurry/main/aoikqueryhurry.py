# coding: utf-8
from __future__ import absolute_import

import os.path
import sys


#
def pythonpath_init():
    #
    my_dir = os.path.dirname(os.path.abspath(__file__))

    #
    for path in ['', '.', my_dir]:
        if path in sys.path:
            sys.path.remove(path)

    #
    pkg_dir = os.path.dirname(my_dir)

    #
    src_dir = os.path.dirname(pkg_dir)

    assert os.path.isdir(src_dir), src_dir

    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)

    #
    dep_dir = os.path.join(pkg_dir, 'dep')

    assert os.path.isdir(dep_dir), dep_dir

    if dep_dir not in sys.path:
        sys.path.insert(0, dep_dir)

#
def main():
    #
    pythonpath_init()

    #
    from aoikqueryhurry.main.main_imp import main as main_func

    #
    return main_func()

#
if __name__ == '__main__':
    sys.exit(main())
