#!/usr/bin/python3

# https://projecteuler.net/problem=3

import math

def primes(number):	
	while True:
		if is_prime(number):
			yield number
		number += 1

def is_prime(number):
	if number == 1:
		return False
	if number == 2:
		return True
	for div in range(3, int(math.sqrt(number)+1), 2):		
		if number % div == 0:
			return False
	return True

def get_prime_factors(n):
	prime = 2 #current prime
	factors = []

	while n > 1:	
		if n % prime == 0: # if n is divisable by the current prime, the prime is a prime factor of the number			
			n //= prime # divide by the prime to check for further prime factors
			factors.append(prime)		
		prime = next(primes(prime+1))	

	return factors

n = 600851475143
factors = get_prime_factors(n)
print(factors)
print(max(factors))