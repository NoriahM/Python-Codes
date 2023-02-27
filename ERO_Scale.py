columns=int(input("Enter Columns"))
rows=int(input("Enter Rows"))
i=0
m=[]
c=0
while (c<rows):
    r=[]
    k=0
    while (k<columns):
        x=int(input("Enter Number"))
        r.append(x)
        k=k+1
    m.append(r)
    c=c+1
p=int(input("enter number to scale matrix"))
for i in range(0,rows):
    for j in range(0,columns):
        t=m[i][j]*p
        m[i][j]=t
h=0        
while (h<rows):
    print(m[h])
    h=h+1

