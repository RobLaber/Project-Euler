# An integer is called increasing/decreasing if no digit is less/greater than the 
# digit to its left.  A number is called bouncy if it is neither increasing nor 
# decreasing.  Find the smallest integer x such that the ratio of bouncy numbers to 
# non-bouncy numbers is exactly 99:1 (i.e., 99%).
#
# Answer: 1587000


def is_incr(i):
	digits =list(map(int, str(i)))
	incr=True
	for i in range(0,len(digits)-1):
		if(digits[i]>digits[i+1]):
			incr=False
			break
	return incr
	
def is_decr(i):
	digits =list(map(int, str(i)))
	decr=True
	for i in range(0,len(digits)-1):
		if(digits[i]<digits[i+1]):
			decr=False
			break
	return decr
	
	
def is_bouncy(i):
	return((not is_decr(i)) and (not is_incr(i)))


bouncy=0.0 # need float to avoid integer division
i=0

while(True):
	i+=1
	if(is_bouncy(i)):
		bouncy+=1.0
	if(bouncy/i ==.99):
		break		
		
print i			
		