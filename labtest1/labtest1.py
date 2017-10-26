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
	lennum=int(log10(num)+1)	#would put +1 here but that would neseseitate a -1 on the very next line
	for i in range(0,lennum):
		numlist.insert(0,num%10)
		num=int(num/10)
	return numlist

def listasnum(list):
	'''the inverse of numaslist'''
	number=0	#all vars are global. using the same name so often is asking for trouble
	multiplicitive=1
	lent=len(list)-1
	while lent>=0:
		number=number+(list[lent]*multiplicitive)
		multiplicitive=multiplicitive*10
		lent=lent-1
	return number


def ishappy(num):
	'''check if a number is happy'''
	numlist=numaslist(num)

topnum=print("Enter a number. All happy numbers upto that number will be printed\nEnter number:")
#no time for error checking, assuming perfect input


