# First, we import a file containing approximately 5000 first names, which we find at
# path Users/robertlaber/Desktop/ProjectEuler/Chal22Names.txt.  Then, we alphabetize the list.  Each
# name is then given its alphanumeric value, i.e., 'Colin' = 3+15+12+9+14 = 53.  Since
# 'Colin' is the 938th name on the list, its overall value is 53*938 = 49714.  Find the 
# sum of all values of the names on the list.  
#
# Answer: Total is 871198282.




file = open('/Users/robertlaber/Desktop/ProjectEuler/Chal22Names.txt')

str=file.readlines()		# returns a list with 1 entry
names=str[0].split(',')		# returns a list of names
alphanames=sorted(names)	# built-in function sorted() returns alphabetized list


total=0	

for j in range(0,len(alphanames)):

	nametotal=0
	
	for i in range (0,len(alphanames[j])):		
		if(ord(alphanames[j][i])>= ord('A') and ord(alphanames[j][i])<= ord('Z')):
			nametotal+=ord(alphanames[j][i])-ord('A')+1
	
	total+=nametotal*(j+1)	
	
print total
