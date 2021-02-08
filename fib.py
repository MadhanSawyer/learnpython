N= int(input("Enter the  value till which Fibonacci series will be generated :"))
def fibb(N):
	t1= 0
	t2= 1
	fib = [0,1]
	t=0
	while t < (N-2):
		fib.append(fib[t1]+fib[t2])
		t1 += 1
		t2 += 1
		t += 1
	return fib

print(fibb(N))