#!/usr/bin/python3

fib = [1,2]

limit = 4000000

while True:
	v = fib[-1] + fib[-2]
	if v < limit:
		fib.append(v)
	else:
		break


even = [x for x in fib if x % 2 == 0]

print(even)
print(sum(even))