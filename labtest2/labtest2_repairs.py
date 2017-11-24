#Requirements: To be added at a better time
#Author: Liam McCormick
#Date: 23/11/17
#OS: Gentoo
#Kernel: Linux 4.13.11
#python version 3.4.5

sep=',' #sepperator, should be same as in file

def importlibrary():
	'''read in list of books from file and save as a dictionary of book classes'''

	booklist=open("books.txt","r")

	list_of_books={}

	for book in booklist.readlines():	#turn the file into a dictionary of book classes
		bookAsList=book.split(',')
		list_of_books[int(bookAsList[0])]=Book(Title=bookAsList[1],Author=bookAsList[2],Price=bookAsList[3])
		#bookAsList[0] is the id, bookAsList[1] is the name, [2] the author and [3] the price

	booklist.close()
	return list_of_books

class Book():
	'''a data structure to store 1 book'''

	def __init__(self,Title,Author,Price):
		self.title=Title
		self.author=Author
		self.price=float(Price)

	def __str__(self):
		'''return a string that looks like the format of the file'''
#		sep=','	#sepperator, should be same as in file
		return self.title+sep+self.author+sep+str(self.price)

	#sets and gets
	def setTitle(self,newname):
		self.title=newname
	def getTitle(self):
		return self.title
	def setAuthor(self,newAuthor):
		self.author=newAuthor
	def getAuthor(self):
		return self.author
	def setPrice(self,Newprice):
		self.price=float(Newprice)
	def getPrice(self):
		return self.price

def addBook(library):
	'''add a book to the library from user input
	santax: library=addbook(library)'''

	id=int(input("Enter an id for the new book: "))	#get id of new book from user

	#if taken
	for i in library:
		if i == id:
			print("Id taken")
			return library

	#else
	name=input("Enter name of new book: ")
	writer=input("Enter the author of that book: ")
	cost=input("Enter the cost of that book: ")

	#different names just in case I got scope mixed up

	library[id]=Book(Title=name,Author=writer,Price=cost)
	return library

def checkAuthor(library,name):
	'''return an author from title of book'''

	#if in library
	for id in library:
		if library[id].title.strip() == name:
			return library[id].author

	#else
	return("Book not found")


def calcprice(library):
	'''calcultate price of all books in library combined'''

	total=0
	for id in library:
		total=total+library[id].getPrice()

	return total


def status(library):
	'''return a string of all books in library'''

	for id in library:
		print(id,library[id])
	print("\n")

def discount(library,ratio):
	'''multiply the price of every item in the library by ratio
	intended santax is library=discount(library,100 - % discount)'''

	for id in library:
		newprice=(library[id].getPrice()/100)*ratio
		library[id].setPrice(newprice)
	return library

def savelib(library,filename):
	'''save modified library to file'''
	file=open(filename,"w+")

	for id in library:
		file.writelines(str(id)+','+library[id].__str__()+"\n")

	file.close()


def main():
	library=importlibrary()

	#check status
	status(library)

	#add a book
	library=addBook(library)

	#check status
	status(library)

	#search for author by book title
	Name=input("Enter the name of a book to check Author: ")
	print(checkAuthor(library,Name))

	#calculate total price of all books
	total=calcprice(library)
	print("total price is",total)

	#apply 10% discount to all books
	print("\napplying discounts")
	library=discount(library,100-10)	#see docstring

	#show status
	status(library)

	#save to books1.txt
	savelib(library,"books1.txt")

if __name__=='__main__':
	main()
