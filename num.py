a = [int(x) for x in input().split()]
i=a[0]
l=a[1]
c=0
for i in range(i,l+1):
    if i%a[2]==0:
        c=c+1
print (c)
