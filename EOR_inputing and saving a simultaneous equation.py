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

h=0        
while (h<u):
    print(m[h])
    h=h+1
