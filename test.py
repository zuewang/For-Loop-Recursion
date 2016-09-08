def fr(set, n):
	if n == 1:
		print set
	else:
		for i in range(0, 3):
			set.append(n*100+i)
			fr(set, n-1)
fr([], 3)

def fr2(set, n):
	if n == 1:
		print set
	else:
		for i in range(0, 3):
			#reset set
			while len(set) > 3 - n:
				set.pop()
			
			set.append(n*100+i)
			fr2(set, n-1)

fr2([], 3)
