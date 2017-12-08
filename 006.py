def diff_of_sums(start,end):
	sum_of_squares = sum([x**2 for x in range(start, end+1)])
	square_of_sum  = sum(range(start,end+1))**2
	return square_of_sum - sum_of_squares

print("1 - 10", diff_of_sums(1,10))
print("1 - 100", diff_of_sums(1,100))