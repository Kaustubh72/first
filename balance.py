a=input()
a=list(a)
l=len(a)
for i in range(l):
    if a[i]=='(' or a[i]=='[' or a[i]=='{':
        for j in range(i+1,l):
            if a[j]==')' or a[j]=='}' or a[j]==']':
                a[i]=a[j]=' '
                break
for i in range(l):
    if a[i]=='(' or a[i]=='[' or a[i]=='{' or a[i]==')' or a[i]=='}' or a[i]==']':
        print(i+1)
        exit(0)
print("Successful")
