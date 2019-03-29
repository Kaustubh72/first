t=int(input())
i=0
k=0
c=[]
j=0
p=0
for i in range(0,t):
    f=0
    a= [str(x) for x in input().split()]
    s=list(a)
    j=len(a[0])
    l=len(a[1])
    for k in range(0,l):
        if s[0][k] in s[1]:
            f=f+1
    if f==l and j==l:
        c.append("YES")
    else:
        c.append("NO")
i=0
for i in range(0,t):
    print(c[i])
