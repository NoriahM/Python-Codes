S=int(input("Enter no of days to stay"))
n=int(input("Enter No. of people on the trip"))
Na=""
Aa=0
y=[]
z=[]
k=n+1
for p in range(1,k):
    Na=input(("enter name of person",p))
    Aa=int(input(("enter age of person" , p)))
    y.append(Na)
    z.append(Aa)
i=0
while (i<n):
    if (n==2):
        M=5000
    elif (n==3):
        M=6000
    elif (n==4):
        M=7000
    elif (n>=5):
        M=1500*n
    if (z[i]<=60):
        T=M*S   
    else:
        t=0.5*(M*S)
    i+=1

print("names",y)
print("ages",z)
print(T)

