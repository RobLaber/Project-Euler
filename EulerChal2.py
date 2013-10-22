# Consider the terms in the Fibonacci sequence that are less than 4 million.  Find the
# sum of those terms that are even.
#
# Answer: 4613732

fib = [1,2]
while(True):
	a=fib[-1]+fib[-2]
	if(a<4000000):
		fib.append(a)
	else:
		break

answer = 0
for num in fib:
	if(num%2 == 0):
		answer+=num
		
print answer					