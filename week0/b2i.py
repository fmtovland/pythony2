#convert binary to an intager

binaryNum=input("Enter a binary number: ")

j=len(binaryNum) - 1	#end condition for loop: count number of 1s and 0s in binary string
i=0			#counter for loop
output=0		#create empty output intager
while(i<=j):
	if binaryNum[i]=='1':
		output=output+(2**(j-i))	#if 1 entered in nth slot, add 2 to the power of n to total
	elif binaryNum[i]=='0':
		output=output			#otherwise, do nothing

	else:	#detect invalid input and exit gracelessly
		print("Error: Non binary number detected")
		print(binaryNum[i])
		quit(1)

	i=i+1	#increment counter

print(output)
