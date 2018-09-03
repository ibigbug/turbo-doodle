import timeit
import random
import implementations

import sys
sys.setrecursionlimit(100000)


def gen_test_data(length=10):
    unsorted_lst = [random.randint(0, length) for i in range(length)]
    sorted_lst = sorted(unsorted_lst)
    reversed_lst = list(reversed(sorted_lst))
    return unsorted_lst, sorted_lst, reversed_lst


def same_order(l1, l2):
    if len(l1) != len(l2):
        return False
    l = len(l1)
    for i in range(l):
        if l1[i] != l2[i]:
            return False
    return True


sorting_funcs = filter(lambda n: not n.startswith('_'), dir(implementations))

print('----------')
for func_name in sorting_funcs:
    unsorted_small, sorted_small, reversed_small = gen_test_data(10)
    unsorted_large, sorted_large, reversed_large = gen_test_data(10000)

    func = getattr(implementations, func_name)

    assert same_order(func(unsorted_small), sorted_small),\
        'sorting failed, %s' % func_name

    t1 = timeit.Timer(lambda: func(unsorted_large))
    print('%s, random, using: %s' % (func_name, t1.timeit(number=1)))

    t2 = timeit.Timer(lambda: func(reversed_large))
    print('%s, reversed, using: %s' % (func_name, t2.timeit(number=1)))

    t3 = timeit.Timer(lambda: func(sorted_large))
    print('%s, orderd, using: %s' % (func_name, t3.timeit(number=1)))

    print('----------')
