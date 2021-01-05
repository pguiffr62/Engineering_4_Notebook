print("Quadratic Solver") 
print("Enter the coefficients for ax^2 + bx + c = 0")

import math
import cmath
def quadratic():
	a=int(input("enter a: "))
	b=int(input("enter b: "))
	c=int(input("enter c: "))
	d=((math.pow(b,2))-(4*a*c)) #calculates discriminant  

	if d<0:
		print("no real roots")
	elif d==0:
		root1 = float(-b + math.sqrt(d))/ (2 * a)
		print("equal roots")
		print(root1)
	elif d>0:
		root1 = (-b + cmath.sqrt(d))/ (2 * a)
		root2 = (-b - cmath.sqrt(d))/ (2 * a) 
		print("real roots")
		print(root1)
		print(root2)
quadratic()

