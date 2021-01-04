import cmath

def doMath():
  operation =input('''
Quadratic Solver
Enter the coefficients for ax^2 + bx + c = 0
''')

a = 1 
b = 5 
c = 6 

# calculating  the discriminant 
dis = (b**2) - (4 * a*c) 
  
# find two results 
ans1 = (-b-cmath.sqrt(dis))/(2 * a) 
ans2 = (-b + cmath.sqrt(dis))/(2 * a) 
  
# printing the results 
print('The roots are') 
print(ans1) 
print(ans2) 

