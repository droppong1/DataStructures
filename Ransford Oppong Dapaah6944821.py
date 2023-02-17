#GitHub link:https://github.com/droppong1/DataStructures.git
#GitHub Username :droppong1
import numpy as np
L=12 #length of beam
w=10 #intensity of UDL
x1=0 #Moment at point where x=0
x2=L #Moment at point where x=L
M1=((-6*(x1**2))+(6*L*x1)-(L**2))/12 #moment when x=0
M2=((-6*(x2**2))+(6*L*x1)-(L**2))/12 #moment when x=l
print(M1) 
print(M2)
V1=(w*(L/2)-x1) #shear force at point where x=0
V2=(w*(L/2)-x2) #shear force at point where x=1
print(V1)
print(V2)

#At point of contraflexure, M=0. ie; (x**2-Lx+L**2/6)=0
#comparing to almighty formula, 
a=1
b=-L
c=L**2/6
#Using the almighty formula
discriminant=b**2-4*a*c
root_1b=(-b+np.sqrt(discriminant))/2*a
root_2b=(-b-np.sqrt(discriminant))/2*a
print(root_1b)
print(root_2b)

#At V=0, x=L/2
x=L/2
print(x)
p = 0
s = 0.01
q = L + s
x = np.arange(p,q,s)
M = (w*(-6*x**2 + 6*L*x-L**2))/12
print(M)

V = w*(L/2 - x)
print(V)

#Let the absolute value of the bending moment array be AM
#Also let the minimum AM be m_AM
AM = abs(M)
m_AM = min(AM)
#When the bending moment is m_AM, we get an expression x**2 - Lx + (L**2/6)+(2*m_AM)/w = 0
#from the above expression
a = 1
b = -L
c = (L**2/6)+(2*m_AM)/w
#Using the Almighty formula the two roots are;
discriminant = b**2 - 4*a*c
root_1f = (-b + np.sqrt(discriminant))/2*a
root_2f = (-b - np.sqrt(discriminant))/2*a
print(root_1f)
print(root_2f)

#Let the relative errors be r_e
r_e1 = ((root_1b - root_1f)/root_1b*100)
r_e2 = ((root_2f - root_2b)/root_2f*100)
print(r_e1)
print(r_e2)

#Let the maximum bending moment be max_M and the minimum bending moment be min_M
#for the maximum
max_M = max(M)
#When the bending moment is max_M, we get an expression x**2 - Lx + (L**2/6)+(2*max_M)/w = 0
a = 1
b = -L
c = (L**2/6)+(2*max_M)/w
#Using the Almighty formula the two roots are;
discriminant = b**2 - 4*a*c
root_1 = (-b + np.sqrt(discriminant))/2*a
root_2 = (-b - np.sqrt(discriminant))/2*a
print(root_1)
print(root_2)
#for the minimum
min_M = min(M)
#When the bending moment is min_M, we get an expression x**2 - Lx + (L**2//6)+(2*min_M)/w = 0
a = 1
b = -L
c = (L**2//6)+(2*min_M)/w
#Using the Almighty formula the two roots are;
#discriminant=b**2-4*a*croot_1=(-b-np.sqrt(discriminant))/2*a
root_1 = (-b - np.sqrt(discriminant))/2*a
root_2 = (-b + np.sqrt(discriminant))/2*a
print(root_1)
print(root_2)
