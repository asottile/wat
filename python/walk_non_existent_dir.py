import os

if __name__ == '__main__':
    # I would hope this oserrors, but alas it does not
    list(os.walk('i_dont_exist'))
