n=int(input())
i=0
a=[]
b=[]
c=[]
for i in range(0,n):
    a.append(int(input()))
i=0
for i in range(0,n):
    if a[i]%12==0:
        c.append(a[i]-11)
        b.append('WS')
    elif a[i]%12==1:
        c.append(a[i]+11)
        b.append('WS')
    elif a[i]%12==2:
        c.append(a[i]+9)
        b.append('MS')
    elif a[i]%12==3:
        c.append(a[i]+7)
        b.append('AS')
    elif a[i]%12==4:
        c.append(a[i]+5)
        b.append('AS')
    elif a[i]%12==5:
        c.append(a[i]+3)
        b.append('MS')
    elif a[i]%12==6:
        c.append(a[i]+1)
        b.append('WS')
    elif a[i]%12==7:
        c.append(a[i]-1)
        b.append('WS')
    elif a[i]%12==8:
        c.append(a[i]-3)
        b.append('MS')
    elif a[i]%12==9:
        c.append(a[i]-5)
        b.append('AS')
    elif a[i]%12==10:
        c.append(a[i]-7)
        b.append('AS')
    elif a[i]%12==11:
        c.append(a[i]-9)
        b.append('MS')
i=0
for i in range(0,n):
    print(c[i],b[i])
