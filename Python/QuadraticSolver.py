print("Quadratic Solver") #prints initial message
print("Enter the coefficients for ax^2 + bx + c = 0")

import math
import cmath
def quadratic():  #quadratic function 
	a=int(input("enter a: ")) #inputs for quadratic values
	b=int(input("enter b: "))
	c=int(input("enter c: "))
	d=((math.pow(b,2))-(4*a*c)) #calculates discriminant  

	if d<0:
		print("no real roots") #if discriminant is < 0 prints no real roots
	elif d==0:
		root1 = float(-b + math.sqrt(d))/ (2 * a)
		print("equal roots") #if discriminant =0 prints one root
		print(root1)
	elif d>0:  #if d is > 0 calulates and prints both roots
		root1 = (-b + cmath.sqrt(d))/ (2 * a) 
		root2 = (-b - cmath.sqrt(d))/ (2 * a) 
		print("real roots")
		print(root1)
		print(root2)
quadratic()

