#Program requirements: Scramble a word/words in sentence.
#Program Author: Liam Mc Cormick
#Date: 28/09/17
#OS: Gentoo
#Kernel: linux 4.9.49-gentoo-r1
#python version: 3.4.5

user_input=input("Enter string to have it scrambled\n")	#get user input
user_input=(user_input+" ..................................")
i=0	#index of first letter of word
j=0	#index of space after word

while i < len(user_input):	#program will loop till i reaches end
	while user_input[j] != (' ' or '.' or ','):
		j=j+1
	j=j-1

	print(user_input[i],end='')	#print first letter of word

	k=j-1	#ensure k not directly mapped to object j
	while(k>i):	#print middle letters of word backwards
		print(user_input[k],end='')
		k=k-1

	print(user_input[j],end=' ')	#print last letter of word

	j=j+2
	i=j+0
	if user_input[j]==".":
		exit()
