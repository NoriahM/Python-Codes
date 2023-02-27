columns=int(input("Enter Columns"))
rows=int(input("Enter Rows"))
i=0
m=[]
c=0
s=[]
while (c<rows):
    r=[]
    k=0
    while (k<columns):
        x=int(input("Enter Number"))
        r.append(x)
        k=k+1
    m.append(r)
    c=c+1  
columns2=int(input("Enter Columns"))
rows2=int(input("Enter Rows"))
i2=0
m2=[]
c2=0
while (c2<rows2):
    r2=[]
    k2=0
    while (k2<columns2):
        x2=int(input("Enter Number"))
        r2.append(x2)
        k2=k2+1
    m2.append(r2)
    c2=c2+1
z=0
while (columns==columns2) and (rows==rows2) and (z<rows):
    while (z<rows):
        y1=[]
        z1=0
        while (z1<columns):
            y=m[z][z1] + m2[z][z1]
            y1.append(y)
            z1=z1+1
        s.append(y1)
        z=z+1
while (i<rows):
    print(s[i])
    i=i+1

    
