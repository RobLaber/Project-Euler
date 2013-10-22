# If the only moves are right and down, how many paths are there from the upper left
# of a 20x20 grid to the lower right?

# The following is a simple recursive method.  The run time is high, but it is a simple
# to the problem.


# def count_paths(n,m):
#	
#		if (n==1 and m==1):
#			return 2
#		if (n==0 or m==0):
#			return 1
#		else:
#			return count_paths(n-1,m)+count_paths(n,m-1)	
#			
# print count_paths(20,20)			


# There is a more fundamental way to attack this problem.  Since our only moves are right
# and down, it must be that to go from the upper left to the lower right, a total of 40
# moves are made, 20 right and 20 down.  Therefore, a path is simply a subset of size 20
# of those moves that will be down, and its complement will be those moves right.  
# Therefore, the total number of distinct paths is the number of distinct subsets of 
# size 20 in a set of size 40.  This can be calculated as 40!/(20!20!) = 137846528820.
# 
# Answer: 137846528820

def factorial(n):
	if (n==1 or n==0):
		return 1
	else:
		return n*factorial(n-1)	

x=factorial(20)*factorial(20)		
print factorial(40)/x		