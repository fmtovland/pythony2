#convert binary to an intager

binaryNum=input("Enter a binary number: ")

j=len(binaryNum) - 1
i=0
output=0
while(i<=j):
	if binaryNum[i]=='1':
		output=output+(2**(j-i))
	elif binaryNum[i]=='0':
		output=output		#do nothing
	else:
		print("Error: Non binary number detected")
		print(binaryNum[i])
		quit(1)

	i=i+1

print(output)
