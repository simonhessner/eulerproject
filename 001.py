#!/usr/bin/python3

def calc_sum(n):
	numbers = [x for x in range(1, n) if x % 3 == 0 or x % 5 == 0]
	return sum(numbers)

print(calc_sum(10))
print(calc_sum(1000))