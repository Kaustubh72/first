a=input()
d=[]
d=list()
d=a.split()
f=1
c=[]
c=list()
d[0]=int(d[0])
for i in range(int(d[1])):
    b=input()
    c=b.split()
    if d[0]>int(c[0]):
        d[0]=d[0]+int(c[1])
    else:
        f=0
if f==0:
    print("NO")
else:
    print("YES")
