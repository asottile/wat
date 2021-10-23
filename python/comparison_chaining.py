"""This has to do with the way python chains comparison operators

This happens in all versions of python I have access to:
- python2.6
- python2.7
- python3.3
- python3.4
- python3.5
"""
from __future__ import print_function

import ast  # noqa (used by eval)


def print_and_run(s):
    print('>>> {0}'.format(s))
    print(eval(s))


def main():
    for s in (
        '(False == False) in [False]',
        'False == (False in [False])',
        'False == False in [False]',
        'ast.dump(ast.parse("False == False in False"))',
        '7 > 6 > 5',
    ):
        print_and_run(s)


if __name__ == '__main__':
    raise SystemExit(main())
