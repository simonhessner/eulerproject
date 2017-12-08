#!/usr/bin/python3

# https://projecteuler.net/problem=7

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

prime = 0
for i in range(10001):
	prime = next(primes(prime+1))

print(prime)