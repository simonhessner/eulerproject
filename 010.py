import operator
import functools
import math

def primes(number):	
	while True:
		if is_prime(number):
			yield number
		number += 1

def is_prime(number):
	if number == 2:
		return True
	if number == 1 or number % 2 == 0:
		return False	
	for div in range(3, int(math.sqrt(number)+1), 2): #skip even divisors
		if number % div == 0:
			return False
	return True

primes_below_2M = list(filter(is_prime, range(2000000)))
print(functools.reduce(operator.add, primes_below_2M, 0))