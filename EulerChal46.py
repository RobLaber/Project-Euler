# Goldbach conjectured that every odd composite integer can be written as the sum of a 
# prime and twice a square.  This conjecture is false.  What is the smallest 
# counterexample?  
#
# Answer: 5777

import math

def smaller_squares(n):     # function returns a list of all 2*i*i less than n
	x=[]					
	i=1
	while(i*i < n/2):
		x.append(2*i*i)
		i+=1
	return x
	
def is_prime(n):			# primality tester.  only needs to check if n is divisible
	prime=True				# by an integer <= sqrt(n) (easy proof)
	i=1
	while(i*i <=n):
		i+=1
		if(n%i==0):
			prime=False
	return prime		

i=11						# initialize at 11.  Why 11?  Well why not?
keepgoing=True
while(keepgoing):
	i+=2						# only check odd integers	
	if(is_prime(i)):			# only check composites
		continue						
	diffs = [i-entry for entry in smaller_squares(i)]   # computes i-2n^2 for 
	winner=True
	for j in diffs:				# now check if any entry is prime.  If not, we have a
		if(is_prime(j)):		# winner!
			winner=False
			break
	if(winner ==True):
		break
print i				
		