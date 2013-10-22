# If 1,1,2 are the first, second, and third Fibonacci numbers, find the n such that 
# the nth Fibonacci number has over 1000 digits.  
#
# Answer: n=4782


e=1
f=1
n=2

while(f<pow(10,999)):			# Recall 10^n is the smallest number with n+1 digits
	
	n+=1
	temp=f
	f+=e
	e=temp

print n	
