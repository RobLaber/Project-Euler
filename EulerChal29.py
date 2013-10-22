# How many distinct terms are there of the form a^b for 2\leq a,b\leq 100?
#
# Answer: 9183


import sets

nums = sets.Set()

for a in range (2,101):
	for b in range(2,101):
		nums.add(pow(a,b))
		
print len(nums)		
