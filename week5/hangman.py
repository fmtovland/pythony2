#program requirements: make hangman in python
#program author: Liam Mc Cormick
#date: 19/10/17
#OS: gentoo
#kernel: linux 4.13.7
#python version: 3.4.5
#requires dictionary.txt, a text file containing lots of words. i used the one from the pip module dictionary
#this might have been a terrible idea as the words in this dictionary are not suitable for anyone but a student of english, but whatever
dicsize=159344	#number of words in dictionary.txt

def drawman(limbs):
	'''draw a hangman with a specified number of limbs'''
	print("---------")
	print("|       |")

	#head
	print("|       ",end='')
	if limbs>0:
		print("O",end='')
	print()

	#body
	print("|      ",end='')
	if limbs>2:
		print("-|",end='')
	elif limbs>1:
		print(" |",end='')
	if limbs>3:
		print("-",end='')
	print()

	#body part 2
	print("|       ",end='')
	if limbs>1:
		print("|",end='')
	print()

	#legs
	print("|      ",end='')
	if limbs>4:
		print("/ ",end='')
	if limbs>5:
		print("\\",end='')
	print()

	#two more |s
	print("|\n|")


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

def printword(word,guesses):
	'''print the secret word with non guessed letters censored to _s'''
	for char in word:
		if char in guesses:
			print(char,end='')
		else:
			print("_",end='')	#oh dear, an emoji. so sorry!
	print()


secretword=genword()		#generate a word for the user to guess at
limbs=0				#number of wrong guesses made
remlets=len(secretword)		#number of letters left to guess
guesses=[]			#letters that have already been guessed

while limbs<6 and remlets!=0:		#break out of loop when all limbs have been drawn
	print("\n")			#space between iterations
	drawman(limbs)			#draw the hangman (not implemented in this revision)
	print("letters guessed:",guesses)
	printword(secretword,guesses)	#see ''' ''' comment

	guesses.append(input("Guess a letter: "))

	if guesses[-1] in secretword:
		remlets=remlets-1
	else:
		limbs=limbs+1

drawman(limbs)
printword(secretword,guesses)

if limbs<6:
	print("You win")
else:
	print("You lose, word was:",secretword)
