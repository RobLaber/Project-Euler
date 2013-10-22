# Find the largest palindrome made from the product of two 3-digit numbers.
#
# Answer: 906609

def is_pal(i):
	s = str(i)
	pal=True
	for j in range(1,len(s)/2+1):
		if(s[j-1] != s[-j]):
			pal=False
			break
	return pal
	
	
pals = []
for i in range(100, 1000):
	for j in range(100,1000):
		if(is_pal(i*j)):
			pals.append(i*j)

print max(pals)		