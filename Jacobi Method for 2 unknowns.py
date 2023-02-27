u=int(input("enter no of unknowns"))
m=[]
print("enter numbers in the form ax + by + cz = d")
for i in range (0,u):
    ua=int(97)
    mh=[]
    print("for equation:",i+1)
    for j in range (0,u+1):
        print("enter" , chr(ua))
        s=int(input())
        ua=ua+1
        mh.append(s)
    m.append(mh)
q=int(input("No of iterations?"))
if (u==2):
    xo=int(0)
    yo=int(0)
    for i in range(0,q):
        x1=(1/m[0][0])*((m[0][2])-(m[0][1]*yo))
        y1=(1/m[1][1])*((m[1][2])-(m[1][0]*xo))
        xo=y1
        yo=x1
        print(xo,yo)
    print("x=",xo)
    print("y=",yo)
