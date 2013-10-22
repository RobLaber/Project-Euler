# Find all positive integers less than 1000 that are multiples of 3 or 5,
# then compute their sum.
#
# Answer: 233168

threes=[]
fives=[]

for i in range(0,1000):
	if (i%3==0):
		threes.append(i)
	if (i%5==0):
		fives.append(i)

nums = set(threes+fives)
answer=0
for num in nums:
	answer+= num
	
print answer	
			