#!/usr/bin/python3

# https://projecteuler.net/problem=4

nums = range(100,1000)

products = [x*y for x in nums for y in nums]
palindromes = filter(lambda numstr : str(numstr) == str(numstr)[::-1], products)

print(max(palindromes))