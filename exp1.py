x=input();
l=len(x);
i=0;f=0;
for i in range(0,l):
    if(x[i]==x[l-1-i]):
        f=1;
    else:
        f=0;
        break;
if f==1:
    print("Yes");
else:
    print("No");
