# Find the sum of all integers which are equal to the sum of the fifth powers
# of their digits.

# Observe that any such integer must be less than 10^6.

# Answer = 443839

nums=[]

for i in range (10,1000000):
	digits=[]
	temp=i
	while(temp>0):
		digits.append(temp%10)
		temp=temp/10	
	if (i == sum(pow(digit,5) for digit in digits)):
		nums.append(i)	
		
print sum(x for x in nums)		


