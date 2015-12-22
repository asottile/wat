"""This one has to do with how the augmented assigment operator is done."""
import contextlib
import traceback


@contextlib.contextmanager
def catchpls():
    try:
        yield
    except Exception:
        traceback.print_exc()


def main():
    # A one-element tuple which contains a list
    print('>>> x = ([1, 2],)')
    x = ([1, 2],)
    # Assigning to the tuple raises as expected
    print('>>> x[0] = 5')
    with catchpls():
        x[0] = 5
    # Still have the original value
    print('>>> x')
    print(x)
    # But...
    print('>>> x[0] += [3]')
    with catchpls():
        x[0] += [3]
    # Wat
    print('>>> x')
    print(x)


if __name__ == '__main__':
    exit(main())
