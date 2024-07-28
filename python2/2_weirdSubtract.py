def weirdSubtract(n,k):
	for i in range(k):
		if n % 10 == 0:
			n=n/10
		else:
			n -=1
	return int(n) 

n,s = input("Enter num and sub : ").split()

print(weirdSubtract(int(n),int(s)))