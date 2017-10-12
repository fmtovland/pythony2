#bubble sort a list
#Author: Liam Mc Cormick
#Date: 12/10/17
#OS: Gentoo
#Kernel: Linux 4.13.4
#Python version: 3.4.5

size=1
mylist=[input("Enter numbers line after line: finish with a zero\n")]
while True:
	tmp=input()
	if tmp=='':
		break
	else:
		mylist.append(tmp)
