"""Apparently you can subclass None's type, wat."""
# This is apparently fixed in 3.6
# And apparently 2.7.11
from __future__ import annotations


class X:
    pass


class Y(X, type(None)):
    """wat"""


def main():
    # It can be instantiated
    my_none = Y()
    # Kinda looks like None
    print('>>> my_none')
    print(my_none)
    # Doesn't is (so happy)
    print('>>> my_none is None')
    print(my_none is None)
    # Doesn't == though
    print('>>> my_none == None')
    print(my_none == None)  # noqa (intentional comparison to None)


if __name__ == '__main__':
    raise SystemExit(main())
