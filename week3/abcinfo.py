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

for line in abcfile:

	if line[0] == 'X':
		print("Id is",line[2:])


#close file
abcfile.close()
