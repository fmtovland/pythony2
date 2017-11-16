#(1) Write a Python class to represent a Rectangle.
#In addition to the standard methods (_ _ init_ _, _ _str _ _, get/set)
#write a method that will calculate the area of a rectangle.
#Test your class by creating few rectangle objects.

#author: Liam McCormick
#Date: 16/11/17
#OS: Gentoo
#Kernel: 4.13.11
#Python version: 3.4.5

class Rectangle():

	def __init__(self,width,height):
		self.Width=width
		self.Height=height

	def setHeight(self,height):
		self.Height=height

	def setWidth(self,width):
		self.Width=width

	def getHeight(self):
		return self.Height

	def getWidth(self):
		return self.Width

	def getArea(self):
		area=self.Width * self.Height
		return area

