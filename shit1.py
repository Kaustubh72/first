import math
n,m=input().split()
n=int(n)
m=int(m)
a=[]
for i in range(n):
    a.append([])
    s=input()
    for j in range(m):
        a[i].append(int(s[j]))
q=int(input())
b=[]
for i in range(q):
    b.append(int(input()))
c=a
d=[]
for i in range(n):
    for j in range(m):
        if c[i][j]==1:
            d.append((i,j))
e=0
f=[]
for i in range(len(d)):
    for j in range(len(d)):
        e=abs(d[i][0]-d[j][0])+abs(d[i][1]-d[j][1])
        if e!=0:
            f.append(e)
for i in range(len(b)):
    g=0
    for j in range(len(f)):
        if b[i]==f[j]:
            g+=1
    if g>0:
        print(int(g/2))
    else:
        print(g)
