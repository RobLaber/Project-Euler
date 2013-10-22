# Assuming there are coins with values 1,2,5,10,20, 50, 100 and 200, how many possible
# combinations of coins are there that total 200?

# while a bit difficult to interpret directly, this code organizes each combination
# based on the largest coin present.  The variable i represents the index of the 
# largest coin to be used.  We organize this way to prevent repeated combinations, i.e.,
# combo 100+50+50 is the same as 50+100+50.

# Answer = 73682


def how_many(n,largest):			# n is desired value, largest is index of largest
									# coin to be used	
	coins = [200,100,50,20,10,5,2,1]
	
	if(n==0):
		return 1
	
	# find the largest coin less than value n
	
	i=0
	while(coins[i]>n):
		i+=1
		
	i=max(i,largest)	# i is now index of largest coin to be used in each combination
	
	# Now for each coin value less than largest, we add that coin to a combination
	# and repeat the process for the remaining value, keeping in mind that we only
	# use coins with value not greater than the coin we just used.
	
	return sum(how_many(n-coins[j],j) for j in range(i,len(coins)))
	
print how_many(200,0)	