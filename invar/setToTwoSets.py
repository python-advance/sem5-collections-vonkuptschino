import random 

def returnSetOfRandom(n):
	return [random.randint(-10, 10) for a in range(n)]

if __name__ == "__main__":
	se = returnSetOfRandom(100)
	pos = []
	neg = []

	for item in se:
		if item > 0:
			pos.append(item)
		elif item < 0:
			neg.append(item)

	print(pos)
	print(neg)


	
