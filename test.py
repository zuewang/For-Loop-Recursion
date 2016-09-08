def fr(set, n):
	if n == 1:
		print set
	else:
		for i in range(0, 3):
			set.append(n*100+i)
			fr(set, n-1)
fr([], 3)