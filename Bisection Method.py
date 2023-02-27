print ("This program solves quadratic equations in the form ax^2+bx+c=0")
a=float(input("ENTER a"))
b=float(input("ENTER b"))       
c=float(input("ENTER c"))

Xl=float(input("Enter Assumption#1 (lower limit)"))
Xu=float(input("Enter Assumption#2 (upper limit)"))
Calc= ((a*(Xl**2))+(b*Xl)+c)*((a*(Xu**2))+(b*Xu)+c)
print(Calc)
end=int(0)
while(Calc != 0) and (end!=100):
    if (Calc < 0):
        Xm=(Xl+Xu)/2
        Calc2=((a*(Xl**2))+(b*Xl)+c)*((a*(Xm**2))+(b*Xm)+c)
        if (Calc2 <0):
            Xu=Xm
        if (Calc2 >0):
            Xl=Xm
    end=end+1
    print(Xl,Xu)
print("Values at which the root lies is approximately equal to" ,Xl,Xu)
    
    
