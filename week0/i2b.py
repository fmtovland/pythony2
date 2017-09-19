#Our task is to convert an integer number to binary, and from binary back to integer. It
#will give us a chance to play with if-elif-else and while statements, as well as a little
#string slicing.

from math import log2

number=input("Enter a number: ")
number=int(number)

biggest=int(log2(number))	#find how many 1s and 0s are in the output
print(biggest)
output=[]

while(biggest>=0):

	if(number-(2**biggest) >= 0):		#biggest at this point is which digit of binary you are currently calculating
		number=number-(2**biggest)
		output.insert(0,'1')

	else:
		output.insert(0,'0')

	biggest=biggest-1

print("in binary that is",end=' ')

i=len(output)
while i>0:
	i=i-1
	print(output[i],end='')

print("")
