#!/usr/bin/python3

# https://projecteuler.net/problem=2
limit = 4000000

def fib(max_fib):
	a, b = 0, 1
	while a < max_fib:
		yield a
		a,b = b,a+b
		# This does not work because a and b depend on each other and cannot be evaluated at the same time without using a temporary variable. a,b = b,a+b 
		# first reads b and a+b and then assigns it to a,b at the same time
		#a = b
		#b = a+b

even = [x for x in fib(limit) if x % 2 == 0]

print(even)
print(sum(even))