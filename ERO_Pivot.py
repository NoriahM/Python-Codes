columns=int(input("Enter Columns"))
rows=int(input("Enter Rows"))
i=0
m=[]
c=0
a=[]
a2=[]
st=[]
while (c<rows):
    r=[]
    k=0
    while (k<columns):
        x=int(input("Enter Number"))
        r.append(x)
        k=k+1
    m.append(r)
    c=c+1
q=int(input("enter number of operations"))
if (q==1):
    sw1=int(input("enter row to apply operation on"))
    p=int(input("enter constant to multipy row to"))
    for j in range(0,columns):
        t=m[sw1-1][j]*p
        m[sw1-1][j]=t
elif (q==2):
    sw1=int(input("enter row to apply operation on"))
    q1=int(input("enter constant to multipy row to"))
    sw2=int(input("enter row to apply second operation on"))
    q2=int(input("enter constant to multipy row to"))
    s1=int(input("store in row number?"))
    for j in range(0,columns):
        t=m[sw1-1][j]*q1
        a.append(t)
    for j in range(0,columns):
        t2=m[sw2-1][j]*q2
        a2.append(t2)
    for j in range(0,columns):
        s=a[j]+a2[j]
        st.append(s)
        m[s1-1]=st
else:
    print("invalid number of operations")
h=0        
while (h<rows):
    print(m[h])
    h=h+1
