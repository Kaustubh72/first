a=input("Enter a word containing lowercase letters only:")
b=[]
b=a.split()
l=len(a)
s=0
for j in range(len(b)):
    a=b[j]
    for i in range(l):
        if a[i].islower():
            o=ord(a[i])-96
            s=s+o
        elif a[i].isupper():
            s=s+ord(a[i])+1
        else:
            s=s+ord(a[i])+1
print(s)
