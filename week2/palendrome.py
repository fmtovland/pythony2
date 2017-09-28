input_word=input("Enter word to check if palendrome: ")	#get input from user
input_word=input_word.lower()	#make all lower case
i=0
wordlen=len(input_word)
word=[]			#create blank array

while i < wordlen:	#remove all puncutation
	if input_word[i].isalpha():
		word.append(input_word[i])
	i=i+1

wordlen=len(word)-1     #the -1 accounts for indexes starting at 0
middle=int(len(word)/2) #calculate index of middle letter

i=0
while(i < middle):
	if word[wordlen-i] is not word[i]:
		print("Thats not a palendrome")
		exit()
	i=i+1

print("That's a palendrome")
