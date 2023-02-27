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

while (i<rows):
    print(m[i])
    i=i+1
