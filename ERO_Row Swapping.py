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

sw1=int(input("enter row to swap"))
sw2=int(input("swap with row?"))
t=[]
i=0
j=0
for j in range(0,columns):
     tx=m[sw1-1][j]
     t.append(tx)
m[sw1-1]=m[sw2-1]
m[sw2-1]=t

h=0
while (h<rows):
    print(m[h])
    h=h+1

        
