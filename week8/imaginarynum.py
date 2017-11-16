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

	def setRealPart(self,rnum):
		'''change the value of the real part of the number'''
		self.Rnum=rnum

	def setImaginaryPart(self,inum):
		'''change the value of the imaginary part of the number'''
		self.Inum=inum


def addInums(inum1,inum2):
	'''add two imaginary numbers together'''

	total=ImaginaryNum(0,0)

	total.setRealPart(rnum=inum1.getRealPart()+inum2.getRealPart())
	total.setImaginaryPart(inum=inum1.getImaginaryPart()+inum2.getImaginaryPart())

	return total

def subInums(inum1,inum2):
	'''subtract two imaginary numbers from oneanother'''

	total=ImaginaryNum(0,0)

	total.setRealPart(rnum=inum1.getRealPart()-inum2.getRealPart())
	total.setImaginaryPart(inum=inum1.getImaginaryPart()-inum2.getImaginaryPart())

	return total
