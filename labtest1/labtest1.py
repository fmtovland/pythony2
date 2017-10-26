#Program requirements: Write a python program that will prompt the user for a number and print all the happy numbers from 1 up to that number. use functions where appropriate to structure your code
#program Author: Liam Mc Cormick
#Date: 26/20/17
#OS: Gentoo
#Kernel: Linux 4.13.7
#Python version: 3.4.5

from math import log10

def numaslist(num):
	'''convert a number to a list of numbers: ie 123 to {1,2,3}'''
	numlist=[]
	lennum=int(log10(num)+1)
	for i in range(0,lennum):
		numlist.insert(0,num%10)
		num=int(num/10)
	return numlist

def listasnum(list):	#thought this was needed. it wasn't. ah well...
	'''the inverse of numaslist'''
	number=0	#all vars are global. using the same name so often is asking for trouble
	multiplicitive=1
	lent=len(list)-1
	while lent>=0:	#calculate most least figure first
		number=number+(list[lent]*multiplicitive)
		multiplicitive=multiplicitive*10
		lent=lent-1
	return number


def ishappy(num):
	'''check if a number is happy'''
	numlist=numaslist(num)	#convert to something indexable with a for loop
	number=0
	while (number != 1) and (number != 4):	#wait till the number defining whether happy or not is reached
		number=0
		for i in range(0,len(numlist)):	#calculate sum of squares
			number=number+(numlist[i]**2)
		numlist=numaslist(number)

	if number == 4:
		return False	#not happy
	elif number == 1:
		return True	#happy
	else:
		return number	#something has most certainly gone wrong


#int main() equivilant starts here
topnum=input("Enter a number. All happy numbers upto that number will be printed\nEnter number: ")	#get top number from user

#I even had time to go back and add some basic input checking
try:
	topnum=int(topnum)
except ValueError:
	print("That was not a freaking number!")
	exit(1)	#unhappy exit

for i in range(1,topnum+1):	#the +1 means from 1 to topnum inclusive
	if ishappy(i):
		print(i,end=', ')	#print all happy numbers

print()	#a neatness line
