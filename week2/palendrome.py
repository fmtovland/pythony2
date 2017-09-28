word=input("Enter word to check if palendrome: ")
i=0
wordlen=int(len(word)/2)
while(i < wordlen):
	if word[wordlen-i] is not word[i]:
		print("Thats not a palendrome")
		exit()
	i=i+1

print("That's a palendrome")
