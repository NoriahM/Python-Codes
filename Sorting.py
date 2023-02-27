a=[]
s=0
i=0
n=int(input("Enter number of values to sort"))
while (i<n):
    s=int(input("enter number"))
    a.append(s)
    i+=1     
x=0
n=len(a)
while (x==0):
    i=0
    while (i<n):
        j=0
        while (j<n):
            if (a[i] < a[j]):
                T=a[i]
                a[i]=a[j]
                a[j]=T
            j=j+1
        i=i+1
        print(a)
    if (max(a)==a[n-1]):
        break

