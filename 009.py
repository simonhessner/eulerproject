from functools import reduce

def is_pythagorian_triplet(a, b, c):
	return a < b < c and a**2 + b**2 == c**2

triplets = []

for a in range(1001):
	for b in range(a, 1001-a):
			triplets.append((a,b,1000-a-b))

matches = filter(lambda x: is_pythagorian_triplet(*x), triplets)
result = reduce(lambda x,y: x*y, list(matches)[0])
print(result)