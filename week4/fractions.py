#program requirements: See fractions.md
#Author: Liam Mc Cormick
#Date: 12/10/17
#OS: Gentoo
#Kernel: Linux 4.13.4
#Python version: 3.4.5

def gcd(bignum,smallnum):
	'''calculate the greatest common devisor of the two numbers using the euclidian algorithm'''
	#ensure the numbskull using this function hasn't confused the arguments
	if bignum<smallnum:
		tmp=bignum
		bignum=smallnum
		smallnum=tmp

	#the function propper robbed from something I did in algorithms last year: C translates quite well to python
	#if you remember python can feely change ints to floats
	third=smallnum
	forth=bignum
	while(forth%third != 0):
		tmp1=int(forth/third)
		tmp2=int(forth-(third*tmp1))
		forth=third
		third=tmp2

	return third

def lcm(bignum,smallnum):
	'''find the lowest common multiple of two numbers'''

	#ensure the numbskull using this function hasn't confused the arguments
	#copied from gcd
	if bignum<smallnum:
		tmp=bignum
		bignum=smallnum
		smallnum=tmp

	comDivisor=gcd(bignum,smallnum)
	answer=(bignum*smallnum)/comDivisor
	return answer
