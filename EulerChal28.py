# If the numbers 1 through 25 are arranged in an outward spiral
#
#      21  22  23  24  25
#      20  7   8   9   10
#      19  6   1   2   11
#	   18  5   4   3   12
#      17  16  15  14  13
#
# Then the sum of the diagonal numbers is 1+9+25+3+13+5+17+7+21 = 101.
#
# What is the sum of the diagonal numbers in a similar grid of size 1001x1001?
#
# Answer: 669171001


total=1
for i in range (1,501):
	total+= 16*i*i+4*i+4
	
print total	