#Our task is to convert an integer number to binary, and from binary back to integer. It
#will give us a chance to play with if-elif-else and while statements, as well as a little
#string slicing.

from math import log2

number=input("Enter a number: ")
number=int(number)

biggest=int(log2(number))	#find how many 1s and 0s are in the output
#print(biggest)			#for debugging
output=[]			#an empty list, which will be populated with 1s and 0s

while(biggest>=0):

	if(number-(2**biggest) >= 0):		#biggest at this point is which digit of binary you are currently calculating
		number=number-(2**biggest)	#subtract the power of two which has already been converted to a binary digit
		output.insert(0,'1')		#add a 1 to the string output

	else:
		output.insert(0,'0')		#add a 0 to the string output

	biggest=biggest-1			#decrement the loops condition

print("in binary that is",end=' ')

i=len(output)
while i>0:	#print the string of binary, backwards
	i=i-1
	print(output[i],end='')

print("")	#print one last \n
