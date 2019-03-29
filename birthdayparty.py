t=int(input())
i=0
c=[]
for i in range(0,t):
    a = [int(x) for x in input().split()]
    if a[1]%a[0]==0:
        c.append("Yes")
    else:
        c.append("No")
i=0
for i in range(0,t):
    print(c[i])
