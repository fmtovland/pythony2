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

def addFrac(frac1,frac2):
	'''add two fractions together
	the fractions should be in the form
	(a,b) with a as the numberator and b
	the denominator'''

	commonDenominator=lcm(frac1[1],frac2[1])

	factor1=commonDenominator/frac1[1]	#the number to multiply the numberator and denominator of the first fraction by
	factor2=commonDenominator/frac2[1]	#	"	"	"	"	"	"	" the second fraction by

	frac1=(frac1[0]*factor2,commonDenominator)
	frac2=(frac2[0]*factor1,commonDenominator)

	answer=(frac1[0]+frac2[0],commonDenominator)
	answer=reduce(answer)

	return answer

def subFrac(frac1,frac2):
	'''subtract one fraction from another
	the fractions should be in the form
	(a,b) with a as the numberator and b
	the denominator'''

	commonDenominator=lcm(frac1[1],frac2[1])

	factor1=commonDenominator/frac1[1]	#the number to multiply the numberator and denominator of the first fraction by
	factor2=commonDenominator/frac2[1]	#	"	"	"	"	"	"	" the second fraction by

	frac1=(frac1[0]*factor2,commonDenominator)
	frac2=(frac2[0]*factor1,commonDenominator)

	answer=(frac2[0]-frac1[0],commonDenominator)
	answer=reduce(answer)

	return answer

def reduce(frac):
	'''simplify a given fraction argument'''

	common=gcd(frac[0],frac[1])

	fraction=(frac[0]/common,frac[1]/common)

	return fraction
