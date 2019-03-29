n=int(input())
a=[]
a=list()
for i in range(n):
    a.append(input())
b=[]
b=list()
z=[]
z=list()
for i in range(n):
    b=a[i].split()
    z.append(b[0])
c={}
d=[]
d=list()
for i in range(n):
    s=0
    b=a[i].split()
    s=int(b[1])*10+int(b[2])*30+int(b[3])*50
    c.update({b[0]:s})
    if s in d:
        s=s
    else:
        d.append(s)
d.sort()
d.reverse()
f=1
m=0
for i in range(len(d)):
    f=f+m
    m=0
    for j in range(n):
        if d[i]==c[z[j]]:
            m=m+1
            print(f,z[j])
            

