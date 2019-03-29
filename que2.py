def inp():
    n=input()
    return n
n=input("Enter any string: ")
while True:
    if n!='':
        break
    else:
        n=inp()
l=[]
l=n.split()
print("1")
if len(l)>1:
    for i in range(len(l)-1):
        print("Enter any string: 1")
