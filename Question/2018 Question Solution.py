f=open("E:\\Noriah\\UNI\\1-SEM\\ICS\\Programs\\Question Data.txt" , "r")
sd=[]
s=[]
p=0
data=f.readline()
#Storing Data
for i in range (1,len(data)):
    data=f.readline()
    field=data.split("\t")
    s.append(field)
for i in range (1,len(s)):
    t=[]
    for j in range (0,6):
        a=s[i][j]
        t.append(a)
    sd.append(t)
print(sd)
#Total Sales
total=0
june=0
july=0
aug=0
for i in range(0,(len(sd))):
    x=int(sd[i][3])*int(sd[i][4])
    
    total=total+x
print("Total=", total)
#Month-wise sales
x=0
for i in range(0,(len(sd))):
    if (int(sd[i][1])==6):
        x=int(sd[i][3])*int(sd[i][4])
        june=june+x
    if (int(sd[i][1])==7):
        x=int(sd[i][3])*int(sd[i][4])
        july=july+x
    if (int(sd[i][1])==8):
        x=int(sd[i][3])*int(sd[i][4])
        aug=aug+x
print("june: ",june)
print("july: ",july)
print("Aug: ",aug)
#Sales Id wise Sales
for i in range (0,11):
    x=0
    t=0
    for j in range (1,(len(sd))):
        if (int(sd[j][5])==i):
            x=int(sd[j][3])*int(sd[j][4])
            t=t+x
    print("salesid:",i,t)
            
             



