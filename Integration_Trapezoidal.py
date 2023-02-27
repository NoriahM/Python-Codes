print("Integration of quadratic equation, enter equation in the form: ax^2 + bx +c = 0")
a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))
A=int(input("Enter first assumed point"))
B=int(input("Enter first assumed point"))
n=int(input("enter no of segments!?"))
x=0
t=0
i=1
fin=0
h=(B-A)/n
t=(((a*((A)**2))+(b*(A)+c))+(((a*((B)**2))+(b*(B)+c))))
while (i<n):
    calc=2*((a*((A+(i*h))**2))+(b*(A+(i*h)+c)))
    t=t+calc
    i=i+1
fin=(t*(h/2))
print("Integral",fin)                             
                              
    
             
