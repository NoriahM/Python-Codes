print("differentiaiton of quadratic equation, enter equation in the form: ax^2 + bx +c = 0")
a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))
de=float(input("Enter delta"))
i=int(input("enter no of iterations!?"))
p=int(input("derivative at point?"))
x=0
while (x<i):
    calc=(((a*((p+de)**2))+(b*(p+de)+c))-((a*((p-de)**2))+(b*(p-de)+c)))/(2*de)
    print(calc)
    de=de/2
    x=x+1
print("Result at" , i , "Iteration" , calc)
