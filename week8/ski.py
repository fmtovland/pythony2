#Write a class to represent an Item - each item has item name, price and quantity. Include a method to calculate total price. Test your class by creating few Item objects.

#author: Liam McCormick
#Date: 16/11/17
#OS: Gentoo
#Kernel: 4.13.11
#python version: 3.4.5

class Item():
	'''an item in a hypothetical shopping kart
	this would have been nice last week!'''

	def __init__(self,name,price,quantity):
		self.Name=name
		self.Price=price
		self.Quantity=quantity

	def setName(self,name):
		'''change the name of the item'''
		self.Name=name

	def setPrice(self,price):
		'''change the price of the item'''
		self.Price=price

	def setQuantity(self,quantity):
		'''change the number of items in the object'''
		self.Quantity=quantity

	def getName(self):
		'''check the name of the item'''
		return self.Name

	def getPrice(self):
		'''check the price of the item'''
		return self.Price

	def getQuantity(self):
		'''check the quantity of the item'''
		return self.Quantity

	def getTotal(self):
		'''check the total cost of all items in the object'''
		Total=self.Price * self.Quantity
		return Total
