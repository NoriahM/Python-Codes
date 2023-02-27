a=[]
s=0
i=0
n=int(input("Enter number of values to add in the list"))
while (i<n):
    s=int(input("enter number"))
    a.append(s)
    i+=1
v=int(input("Enter number to be searched"))
i=0
f="n"
while (i<len(a)):
    if(a[i]==v):
        print("Found at position: ", i+1)
        f="y"
    i=i+1
if(f!="y"):
    print("Not Found")
        
