# Find the largest prime factor of 600851475143.
#
# Answer: 6857

def is_prime(i):
	prime = True
	j=2
	while(j*j <=i):
		if(i%j==0):
			prime=False
			break
		else:
			j+=1
	return prime
	
x=600851475143		
j=2
while(j*j <=x):
	if(x%j==0 and is_prime(j)):
		biggest = j
	j+=1
print biggest		