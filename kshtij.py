t=int(input())
dmain=dict()
for i in range(0,t):
    z=input()
    dmain[z]=0
    x=input()
    level1=x.split()
    d=dict()
    for j in range(0,len(level1)):
        d[level1[j]]=""
    #print(d)
    for j in range(0,len(level1)):
        y=input()
        level2=y.split()
        for k in range(0,len(level2)):
            if k!=0: 
                d[level2[0]]+=level2[k]
                d[level2[0]]+=" "
    #print(d)
    keys1=list(d.keys())
    items=list(d.values())
    #print(items)
    for k in range(0,len(items)):
        v=items[k].split()
        d[keys1[k]]=v
    #print(d)          
    #print(d)
    dmain[z]=d
keys0=list(dmain.keys())
check0=input()
check1=input()
check2=input()
flag0=0
flag1=0
flag2=0
fur0=""
fur1=""
#print(dmain)
for i in range(0,len(keys0)):
    if check0==keys0[i]:
        flag0=1
        break
fur0=check0
#print(fur0)
#print(dmain[fur0])
finalkeys=list(dmain[check0].keys())
#print(finalkeys)
if flag0==1:
    for i in range(0,len(finalkeys)):
        if finalkeys[i]==check1:
            flag1=1
            break
    fur1=check1
    #print(fur1)
    if flag1==1:
        for i in range(0,len(dmain[fur0][fur1])):
            if dmain[fur0][fur1][i]==check2:
                flag2=1
        if flag2==1:
            print("Taxonomy present")
        else:
            print("Taxonomy not present")
    else:
        print("Taxonomy not present")
else:
    print("Taxonomy not present")
