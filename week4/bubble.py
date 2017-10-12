#bubble sort a list
#Author: Liam Mc Cormick
#Date: 12/10/17
#OS: Gentoo
#Kernel: Linux 4.13.4
#Python version: 3.4.5

def bsort(listToSort):
	'''bubble sort a list then return the sorted list'''

	cont=False
	while cont==False:
		cont=False
		for i in range(0,len(listToSort)-2):	#go through the list once; the -2 is one to account for counting from 0 and one to ensure this process only continues till the penultimate 
			if listToSort[i] > listToSort[i+1]:
				tmp=listToSort[i]
				listToSort[i] = listToSort[i+1]
				listToSort[i+1]=tmp
				cont=True

	return listToSort

size=1
mylist=[]
tmp=input("Enter numbers line after line: finish with an empty line\n")
while tmp != '':
	mylist.append(tmp)
	tmp=input()

#done with tmp here so safe to use elsewhere

mylist=bsort(mylist)	#bsort will be a funtion to bubble sort

print(mylist)	#print sorted list


