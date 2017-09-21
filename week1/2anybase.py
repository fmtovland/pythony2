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

print(number,"in base",base,"is",output)
