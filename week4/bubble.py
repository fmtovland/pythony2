#bubble sort a list
#Author: Liam Mc Cormick
#Date: 12/10/17
#OS: Gentoo
#Kernel: Linux 4.13.4
#Python version: 3.4.5

size=1
mylist=[]
tmp=input("Enter numbers line after line: finish with an empty line\n")
while tmp != '':
	mylist.append(tmp)
	tmp=input()

bsort(mylist)	#bsort will be a funtion to bubble sort

print(mylist)	#print sorted list

#def
