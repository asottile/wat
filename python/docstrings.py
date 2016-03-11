"""foo"""


def f():
    """bar"""

    print(__doc__)


def g():
    print(__doc__)


class C(object):
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
