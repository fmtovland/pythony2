#convert a number to any base

number=input("Enter number: ")
base=input("Enter base to convert to: ")
base=int(base)	#convert base to intager

output=[]
output.append(int(number))

i=0
while output[i]>base:
	output.append(0)
	while output[i]>base:
		output[i+1]=output[i+1]+1
		output[i]=output[i]-base

#print(number,"in base",base,"is",output)	#good for debug, but prints backward

#print the output reversed
i=len(output) - 1
while i>= 0:
	print(output[i],end='')
	i=i-1

#final \n
print("")
