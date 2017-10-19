#program requirements: make hangman in python
#program author: Liam Mc Cormick
#date: 19/10/17
#OS: gentoo
#kernel: linux 4.13.7
#python version: 3.4.5
#requires dictionary.txt, a text file containing lots of words. i used the one from the pip module dictionary
#this might have been a terrible idea as the words in this dictionary are not suitable for anyone but a student of english, but whatever
dicsize=159344	#number of words in dictionary.txt

def genword():
	'''return a random word from dictionary.txt'''
	from random import randint	#for generating a random number

	dictionary=open("dictionary.txt","r")
	wordnum=randint(1,dicsize)
	dictionary.seek(wordnum)
	word=dictionary.readline()
	dictionary.close()
	if len(word)<4:
		word=genword()	#recall the function if it fails
	else:
		word=word[:-1]	#chop the \n off the end

	return word
