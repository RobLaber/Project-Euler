# Find the smallest integer x such that the integers x,2x,3x,4x,5x and 6x all contain
# the same set of digits.  Here, we will use a hash function on the set of digits.
#
# Answer: 142857


def to_digits(i):
	x=list(map(int,str(i)))
	return x

# Our hash takes an integer and interprets each digit of that integer as the index
# of a prime number in primes[] below.  The function then computes the product of the
# primes corresponding to the digits in the input integer.  Thus, two integers have the
# same hash value if and only if they have the same det of digits.

def hash(x):
	primes = [2,3,5,7,11,13,17,19,23,29]
	value=1
	for num in x:
		value*=primes[num]
	return value

i=0
while(True):
	i+=1
	if(hash(to_digits(i)) == hash(to_digits(2*i))):
		if(hash(to_digits(i)) == hash(to_digits(3*i))):
			if(hash(to_digits(i)) == hash(to_digits(4*i))):
				if(hash(to_digits(i)) == hash(to_digits(5*i))):
					if(hash(to_digits(i)) == hash(to_digits(6*i))):
						break
print i					