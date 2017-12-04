#!/usr/bin/python3

calc_sum = lambda n : sum([x for x in range(1, n) if x % 3 == 0 or x % 5 == 0])

assert calc_sum(10) == 23
print(calc_sum(1000))