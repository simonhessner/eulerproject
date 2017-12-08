#!/usr/bin/python3

# https://projecteuler.net/problem=5

import math

def greatest_common_divisor(a,b):
	while b > 0:
		a, b = b, a%b
	return a

def smallest_multiple(start, end):
	result = 1	
	divisors = [x for x in range(start,end+1)]

	for i in divisors:
		result *= i // greatest_common_divisor(i,result)

	return result

	


print(smallest_multiple(1,10))
print(smallest_multiple(1,20))