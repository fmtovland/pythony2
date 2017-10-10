#Program requirements:	Write a program that generates the Fibonacci numbers. Your program should ask
#			the user how many Fibonacci numbers to generate. Try and use functions
#Program author: Liam Mc Cormick
#Date: 10/10/17
#OS: Gentoo
#Kernel: Linux 4.13.4
#Python version: 3.4.5

def calcnums(numofnums):
	""" This function will return a list of numofnums fibonacci numbers, unless the number is nevgitive in which case it returns a string reading "error" """

	if numofnums<1:
		return "error"

	else:
		listofnos=[0,1]
		for i in range(2,numofnums):
			listofnos.append(listofnos[-1]+listofnos[-2])
		return listofnos

numno=input("How many fibonacci numbers do you wish to see?  ")
try:
	numno=int(numno)

except ValueError:
	print("Digits only numbskull!")
	quit()

#generate numbers here
numlist=calcnums(numno)

print(numlist)	#numlist will be a list of fibonacci numbers


