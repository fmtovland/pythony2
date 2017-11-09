#Program requirements: simulate a shopping cart
#Author: Liam Mc Cormick
#date: 8/11/17
#OS: Gentoo
#Kernel: 4.13.11
#python version: 3.4.5

#define type variables
productlist="productlist.txt"	#the filename of the stockfile

def getstock():
	'''import the stock list'''

	stockfile=open(productlist,"r")

	mydict={}

	for line in stockfile.readlines():
		if line[0:2].strip() == "id":
			id=line.strip()[-4:]
			mydict[id]={}
		elif line[0:4].strip() == "name":
			mydict[id]["name"]=line.strip()[6:]
		elif line[0:5].strip() == "stock":
			mydict[id]["stock"]=line.strip()[7:]
			mydict[id]["stock"]=int(mydict[id]["stock"])
		elif line[0:5].strip() == "price":
			mydict[id]["price"]=line.strip()[7:]
			mydict[id]["price"]=float(mydict[id]["price"])

	stockfile.close()
	return mydict

def savestock(mydict):
	'''takes a list of remaining stock and saves it to file'''

	stockfile=open(productlist,"w+")
	for id in mydict:
		string="id: "+id+"\n"
		stockfile.write(string)

		string="name: "+mydict[id]["name"]+"\n"
		stockfile.write(string)

		string="stock:"+str(mydict[id]["stock"])+"\n"
		stockfile.write(string)

		string="price:"+str(mydict[id]["price"])+"\n"
		stockfile.write(string)

		stockfile.write("\n")

	stockfile.close()

def showcon(available,incart):
	'''print the contents of a shopping basket'''
	#note: while it doesn't appear in this revision of the program, a shopping basket is a dictionary of product ids with the number of said product ordered as the referenced element
	#eg {'123c',7} would be 7 Blue shirts
	total=0
	for productId in incart:
		if productId in incart:
			print(incart[productId],"x",available[productId]["name"],"@",available[productId]["price"],"each")
			total=total+(incart[productId]*available[productId]["price"])

	print("costing",total)
	return total

def main():
	'''main block'''
	availableItems=getstock()	#get a list of all available items
	cart={}				#create empty shopping cart

	selection=-1
	while selection != 0:
		print("Your basket contains:")
		showcon(availableItems,cart)
		print("\n")

		print("The following items are available")
		i=1
		idlist=[]
		for id in availableItems:
			if availableItems[id]["stock"] > 0:
				print((str(i)+":"),availableItems[id]["name"],"x",availableItems[id]["stock"])
				i=i+1
				idlist.insert(i,id)
		print("\n")

		selection=input("Press 0 to checkout. Press any other number to add an item to cart: ")
		try:
			selection=int(selection)
		except ValueError:
			selection=-1

		if selection < 0 or selection > i:
			print("bad item number")

		elif selection > 0:
			id=idlist[selection-1]
			amount=input("How many of that item would you like?: ")
			try:	#add amount of item to cart
				amount=int(amount)
				if amount>0 and amount<=availableItems[id]["stock"]:
					availableItems[id]["stock"]=availableItems[id]["stock"]-amount
					cart[id]=cart[id]+amount
				elif amount>availableItems[id]["stock"]:
					print("insufficent stock")
				else:
					print("Invalid amount")

			except ValueError:
				print("Invalid amount")

			except KeyError:
				cart[id]=amount

		else:
			print("checking out")
			areyousure='?'
			while areyousure not in ['y','Y','n','N']:
				areyousure=input("have correct credit card details been entered (Y/N/y/n): ")

			if areyousure == 'y' or areyousure == 'Y':
				savestock(availableItems)
				print("your receipt:")
				profit=showcon(availableItems,cart)
				profits=open("profits.txt","a+")
				profits.write(("profit of "+str(profit)))
#				profits.close()

			elif areyousure == 'n' or areyousure == 'N':
				print("well that was a waste of time")

if __name__ == "__main__":
	main()
