#Program requirements: Write a program to read from a file and print
#the Id, title (first only), time and key signatures line by line.
#Program author: Liam McCormick
#Date: 05-10-17
#OS: Gentoo
#Kernel: linux 4.13.4 (They finally fixed the dualshock drivers)
#python version: 3.4.5

#get filename from command line
import sys
filename=sys.argv[1]	#make the last argument be the filename

#open file for reading
abcfile=open(filename,"r")

title=True	#ensure only the first title is printed

for line in abcfile:

	if line[0] == 'X':
		print("\nId is",line[2:-1],"...",end=' ')	#line sepperator declared here
		title=True				#ensure only the first title is printed

	elif line[0] == 'T' and title==True:
		print("Title is",line[2:-1],"...",end=' ')
		title=False

	elif line[0] == 'K':
		print("Key signature is",line[2:-1],"...",end=' ')

	elif line[0] == 'M':
		if line[2]=="C":
			print("Time signature is commontime ...",end=' ')
		else:
			print("Time signature is",line[2:-1],"...",end=' ')

print()	#print one last line

#close file
abcfile.close()
