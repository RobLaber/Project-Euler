# Find the smallest number that is divisible by every integer from 1 to 20.
# In other words, find the lcm of {1,...,20}

# 2=2
# 3=3
# 4= 2^2
# 5=5
# 6=2*3
# 7=7
# 8=2^3
# 9=3^2
# 10=2*5
# 11=11
# 12=2^2*3
# 13=13
# 14=2*7
# 15=3*5
# 16=2^4
# 17=17
# 18=2*3^2
# 19=19
# 20=2^2*5

# therefore, lcm is 2^4*3^2*5*7*11*13*17*19

print 2**4*3**2*5*7*11*13*17*19