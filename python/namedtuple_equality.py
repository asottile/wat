import collections


A = collections.namedtuple('A', ('b', 'c'))
B = collections.namedtuple('B', ('d', 'e'))


def print_and_run(s):
    print('>>> {}'.format(s))
    print(eval(s))


print_and_run('A(1, 2)')
print_and_run('B(1, 2)')
print_and_run('A(1, 2) == B(1, 2)')


OUTPUT = '''\
>>> A(1, 2)
A(b=1, c=2)
>>> B(1, 2)
B(d=1, e=2)
>>> A(1, 2) == B(1, 2)
True
'''
