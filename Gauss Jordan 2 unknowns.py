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
while (u==2):
            if (m[0][1]!=1):
                i=0
                for i in range(0,1):
                    t=m[1][i]
                    calc=t/m[0][i]
                    m[0][i]=((calc*m[0][i])/m[1][i])
            elif (m[1][0]!=1):
                i=0
                for i in range(0,1):
                    t=m[0][i]
                    calc=t/m[1][i]
                    m[1][i]=((calc*m[1][i])/m[0][i])
            elif (m[0][0]!=0):
                i=0
                for i in range(0,1):
                    calc0=m[0][i]-m[1][i]
                    calc1=calc0-m[0][i]
                    calc2=m[0][i]*(calc1/m[0][i])
                    calc3=calc2+m[1][i]
                    m[0][i]=(calc3)
            elif (m[1][1]!=0):
                i=0
                for i in range(0,1):
                    calc0=m[1][i]-m[0][i]
                    calc1=calc0-m[1][i]
                    calc2=m[1][i]*(calc1/m[1][i])
                    calc3=calc2+m[0][i]
                    m[1][i]=(calc3)
            else :
                break
    
h=0        
while (h<u):
    print(m[h])
    h=h+1
