"""foo"""
from __future__ import annotations


def f():
    """bar"""

    print(__doc__)


def g():
    print(__doc__)


class C:
    """baz"""

    x = __doc__

    def c(self):
        print(__doc__)

    def d(self):
        print(self.x)


if __name__ == '__main__':
    f()
    g()
    C().c()
    C().d()
