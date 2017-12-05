#!/usr/bin/python3

# https://projecteuler.net/problem=3

def get_primes(number):	
	while True:
		if is_prime(number):
			yield number
		number += 1

def is_prime(number):
	if number == 1:
		return False
	for div in range(2, number):		
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
		prime = next(get_primes(prime+1))	

	return factors

n = 600851475143
factors = get_prime_factors(n)
print(factors)
print(max(factors))