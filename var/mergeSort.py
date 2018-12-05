import random 

def returnSetOfRandom(n):
	return [random.randint(0, 10) for a in range(n)]

def mergeSort(a):       
	def mergeGroup(a, left, m, right):
		if left >= right: return None
		if m < left or right < m: return None
		t = left
		for j in range(m+1, right+1):
			for i in range(t, j):
				if a[j] < a[i]:
					r = a[j]
					for k in range(j, i, -1):
						a[k] = a[k - 1]
					a[i] = r
					t = i
					break
	if len(a) < 2: return None
	k=1
	while k<len(a):
		g=0
		while g<len(a):
			z = g + k + k - 1
			r = z if z < len(a) else len(a) - 1
			mergeGroup(a, g, g + k - 1, r)
			g+=2*k
		k*=2
	return a

if __name__ == "__main__":
	se = returnSetOfRandom(1000)
	print(se)
	print(mergeSort(se))


	
