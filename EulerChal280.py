# An ant begins at the center square of a 5x5 grid.  At each step, the ant moves to an
# adjacent square randomly.  There is a seed at each of the bottom 5 squares.  If the 
# is not carrying a seed and moves to a square with a seed, if pick up the seed.  If the
# and is carrying a seed and reaches one of the top 5 squares that does not already have 
# seed on it, the ant puts the seed down.  What is the expected number of steps for the
# ant to move all 5 seeds to the top row?

# To implement the grid, we use the following layout:
#
#
#		1  2  3  4  5
#		6  7  8  9  10
#		11 12 13 14 15
#		16 17 18 19 20
#		21 22 23 24 25	

#
# This algorithm does not yet compute the correct answer.  Further analysis is needed to
# compute the precise expected value.	

import random

def move_from(n):		# n is the current position of the ant.
	
	x= random.random()
	
	if(n in [7,8,9,12,13,14,17,18,19]):
		if(x<.25):
			return n-5
		if(x>=.25 and x<.5):
			return n-1
		if(x>=.5 and x<.75):
			return n+1
		if(x>=.75):
			return n+5
	
	if(n in [2,3,4]):
		if(3*x <1):
			return n-1
		if(3*x>=1 and 3*x <2):
			return n+5
		if(3*x >=2):
			return n+1	
	
	if(n in [6,11,16]):
		if(3*x <1):
			return n-5
		if(3*x>=1 and 3*x <2):
			return n+5
		if(3*x >=2):
			return n+1	
			
	if(n in [10,15,20]):
		if(3*x <1):
			return n-1
		if(3*x>=1 and 3*x <2):
			return n+5
		if(3*x >=2):
			return n-5
	
	if(n in [22,23,24]):
		if(3*x <1):
			return n-5
		if(3*x>=1 and 3*x <2):
			return n-1
		if(3*x >=2):
			return n+1	
			
	if (n==1):
		if(x<.5):
			return 2
		if(x>=.5):
			return 6	
			
	if (n==5):
		if(x<.5):
			return 4
		if(x>=.5):
			return 10
			
	if (n==21):
		if(x<.5):
			return 22
		if(x>=.5):
			return 16
			
	if (n==25):
		if(x<.5):
			return 24
		if(x>=.5):
			return 20

def run_exp():
	
	has_seeds = [21,22,23,24,25]
	needs_seeds=[1,2,3,4,5]
	ant_seed =False	
	
	pos=13
	num_moves=0
	while(len(needs_seeds)>0):
		pos = move_from(pos)
		num_moves+=1
		if(pos in has_seeds and ant_seed==False):
			ant_seed =True
			has_seeds.remove(pos)
		if(pos in needs_seeds and ant_seed==True):
			ant_seed = False
			needs_seeds.remove(pos)
		
	return num_moves

totals=[]	
for i in range (0,1000000):
	totals.append(run_exp())

x=sum(num for num in totals)

print x/1000000.0				
			
																							