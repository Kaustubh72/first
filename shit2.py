import sys
n=int(input())
a=[]
r=0
f=0
for i in range(n):
    a.append(int(input()))
for i in range(n-1):
    for j in range(n):
        p=a[i]
        q=a[j]
        si=0
        sj=0
        if i!=j:
            while(p>0):
                r=p%10
                si=si*10+r
                p=int(p/10)
            while(q>0):
                r=q%10
                sj=sj*10+r
                q=int(q/10)
            if si==sj:
                print(a[j])
                a[j]=0
                f=1
if f==0:
    print("No sum-equivalent")
