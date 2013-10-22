# When written out, the numbers 1-5 are one, two, three, four, five.  The total number
# of characters needed is 3+3+5+4+4 = 19.  Excluding spaces, hyphens, but including
# 'and' as in 'one hundred and three,' how many characters are needed for all numbers
# between 1 and 1000 (inclusive)?  
#
# Answer: 21124


def to_word(n):
	if(n==1):
		return 'one'
	if(n==2):
		return 'two'
	if(n==3):
		return 'three'
	if(n==4):
		return 'four'
	if(n==5):
		return 'five'
	if(n==6):
		return 'six'
	if(n==7):
		return 'seven'
	if(n==8):						
		return 'eight'
	if(n==9):
		return 'nine'
	if(n==0):
		return ''			
	
	
def to_string(n):
	s=list(map(int,str(n)))
	if(len(s)==3):
		if(s[1]==0 and s[2]==0):
			return to_word(s[0])+'hundred'
		else:	
			return to_word(s[0])+'hundredand'+to_string(int(str(s[1])+str(s[2])))
	if(len(s)==2):
		if(s[0]==1):
			if(s[1]==0):
				return 'ten'
			if(s[1]==1):
				return 'eleven'
			if(s[1]==2):
				return 'twelve'
			if(s[1]==3):
				return 'thirteen'
			if(s[1]==5):
				return 'fifteen'
			if(s[1]==8):
				return 'eighteen'
			else:
				return to_word(s[1])+'teen'
		if(s[0]==2):
			return 'twenty'+to_word(s[1])
		if(s[0]==3):
			return 'thirty'+to_word(s[1])
		if(s[0] ==4):
			return 'forty'+to_word(s[1])
		if(s[0]==5):
			return 'fifty'+to_word(s[1])
		if(s[0] ==6):
			return 'sixty'+to_word(s[1])
		if(s[0]==7):
			return 'seventy'+to_word(s[1])
		if(s[0]==8):
			return 'eighty'+to_word(s[1])
		if(s[0]==9):				
			return 'ninety'+to_word(s[1])	
	if(len(s)==1):
		return to_word(s[0])
total=0		
for i in range (1,1000):
	total+=len( to_string(i))
	
print total+11			# need to include 'one thousand'
	
			
		
																