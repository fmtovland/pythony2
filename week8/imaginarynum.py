#Write a class to represent a complex number. Complex numbers can
#be written in the form of a+bi where a and b are real numbers and
#i is the solution of i^2=-1 Add methods to add and subtract complex
#numbers - to add/subtract complex numbers you add/subtract the
#corresponding real and imaginary parts. For example, adding 1+2i
#and 2+3i will result in 3+5i

#author: Liam McCormick
#Date: 16/11/17
#OS: Gentoo
#Kernel: 4.13.11
#python version: 3.4.5

class ImaginaryNum():
	'''a class to represent an imaginary number'''

	def __init__(self,rnum,inum):
		'''Rnum is the real part of the number, inum is the imaginary'''
		self.Rnum=rnum
		self.Inum=inum

	def __str__(self):
		'''return the imaginary number as a string'''
		return (str(self.Rnum)+"+"+str(self.Inum)+"i")

	def getRealPart(self):
		'''retrieve the real part of the number'''
		return self.Rnum

	def getImaginaryPart(self):
		'''retrieve the imaginary part of the number'''
		return self.Inum
