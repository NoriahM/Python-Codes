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
ct=[]
while (rows==columns2)and (columns==rows2):
    r=0
    while(r<rows):
        c=0
        cc=[]
        while(c<columns2):
            s=0
            k=0
            while(k<rows2):
                t=(m[r][k])*(m2[k][c])
                s=s+t
                k=k+1
            cc.append(s)
            c=c+1
        ct.append(cc)
        r=r+1
    if(r==rows):
        break
w=0
while (w<rows):
    print(ct[w])
    w=w+1

            
    
