import itertools
a=input()
a=list(a)
c=[]
for i in range(len(a)+1):
    b=list(itertools.combinations(a,i))
    b.sort()
    for j in range(len(b)):
        if b[j] in c:
            continue
        else:
            c.append(b[j])
l=len(c)
print(l-1)
