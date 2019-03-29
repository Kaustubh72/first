import sys
max=int(input())
n=int(input())
b=[]
b.append([])
for i in range(n):
    a=[]
    r,s=input().split()
    a.append(i+1)
    a.append(r)
    a.append(s)
    b.append(a)
idx=int(input())
pm=input()
f=0
for i in range(n+1):
    if b[idx][1]==pm:
        f=f+1
        break
    else:
        idx=int(b[idx][2])
        f=f+1
        if idx==0:
            break
p=(1-0.02*(f-1))*max
print("{:.2f}".format(p))
