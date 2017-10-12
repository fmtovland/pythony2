Lab Exercise – Functions
Exercise: We are going to work on building functions for our own data structure. We
will build operations for Rational Numbers, or Fractions. We will be able to add,
subtract two fractions and reduce a fraction to its simplest form.
Your Task: Represent a fraction as a 2 element tuple. The first element of the tuple
is the numerator, and the second element is the denominator. Write five functions to
support this new data type
 gcd(bigger,smaller)
gcd (short for greatest common divisor) takes two integers: the first
parameter is larger than the second. gcd returns the integer greatest common
divisor of the two numbers. The famous algorithm for this is Euclid’s
Algorithm.
For example, gcd(60,18) is 6. gcd(121,22) is 11. See
http://en.wikipedia.org/wiki/Euclid_algorithm
 lcm(first,second)
lcm (short for least common multiple) takes two integer parameters and
returns the integer lcm of the two numbers. For example, lcm(4,6) is 12.
lcm(12,20) is 60. You use the lcm to find a common denominator that allows
you to add two fractions.
Use the web to find the formula for the lcm in terms of the gcd. Uses gcd.
 addFrac(frac1,frac2).
addFrac takes two fraction parameters (two tuples, each with a numerator and
an denominator) and returns a fraction that represents the sum of the two
input fractions.
For example, given frac1=(1,4) and frac2=(1,3), then addFrac(frac1,frac2)
returns (7,12). addFrac((2,5),(1,6)) returns (17,30). Uses lcm
 subFrac(frac1,frac2).
subFrac takes two fraction parameters (two tuples, each with a numerator and
a denominator) and returns a fraction that represents the difference between
the first and second fraction.
For example, given frac1=(1,4) and frac2=(1,3), subFrac(frac1,frac2) returns
(-1,12). subFrac((2,5),(1,6)) returns (7,30). Uses lcm
 reduce(frac).
reduce takes a single fraction parameter and returns a fraction. The returned
fraction is the simplest form of a fraction.
For example, given frac=(16,24), reduce(frac) returns (2,3). reduce((100,5))
returns (20,1). Uses gcd
