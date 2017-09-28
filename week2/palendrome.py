word=input("Enter word to check if palendrome: ")
i=0
wordlen=len(word)-1	#the -1 accounts for indexes starting at 0
middle=int(len(word)/2)
while(i < middle):
	if word[wordlen-i] is not word[i]:
		print("Thats not a palendrome")
		exit()
	i=i+1

print("That's a palendrome")
