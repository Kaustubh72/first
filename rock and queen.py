rr=int(input())
cr=int(input())
rq=int(input())
cq=int(input())
a=[]
b=[]
for i in range(1,9):
    a.append([rr,i])
    a.append([i,cr])
a.remove([rr,cr])
i=1
for i in range(1,9):
    b.append([rq,i])
    b.append([i,cq])
i=1
while (rq-i>0 and cq-i>0):
    b.append([rq-i,cq-i])
    i=i+1
i=1
while (rq+i<9 and cq-i>0):
    b.append([rq+i,cq-i])
    i=i+1
i=1
while (rq-i>0 and cq+i<9):
    b.append([rq-i,cq+i])
    i=i+1
i=1
while (rq+i<9 and cq+i<9):
    b.append([rq+i,cq+i])
    i=i+1
i=1
f=[]
for i in range(len(a)):
    if a[i] in b:
        f.append(a[i])
f.sort()
if [rr,cr] in f:
    f.remove([rr,cr])
if [rq,cq] in f:
    f.remove([rq,cq])
for i in range(len(f)):
    for j in range(1):
        p=(f[i][j],f[i][j+1])
        print(p)
