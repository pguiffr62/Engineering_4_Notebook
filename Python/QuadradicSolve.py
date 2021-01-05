print('Quadratic Solver') 
print('Enter the coefficients for ax^2 + bx + c = 0')

import math
import cmath

a=int(input("enter a: "))   #inputs for quad solver
b=int(input("enter b: "))
c=int(input("enter c: "))   

Quadratic(a,b,c): 

discriminant=((math.pow(b,2))-(4*a*c)) #calculates discriminant  

	if discriminant<0:
       		print('no real roots')

	else:
		print('it is real')
   
# find two results
ans1 = (-b-cmath.sqrt(d))/(2 * a) 
ans2 = (-b + cmath.sqrt(d))/(2 * a) 
  
# printing the results 
print('The roots are') 
print(ans1) 
print(ans2)
