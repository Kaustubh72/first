string=input()
shift=int(input())
l=len(string)
i=0
num=0
n=[]
n=list()
for i in range(0,l):
    if string[i].isalnum()==True:
        if ord(string[i])>47 and ord(string[i])< 58:
            s=shift%10
            num=ord(string[i])+s
            if num>57:
               num=47+num%57
        elif ord(string[i])>64 and ord(string[i])< 91:
            s=shift%26
            num=ord(string[i])+s
            if num>90:
                num=num%90+64
        elif ord(string[i])>96 and ord(string[i])< 123:
            s=shift%26
            num=ord(string[i])+s
            if num>122:
                num=96+num%122
        n.append(chr(num))
    elif string[i].isalnum()==False:
        n.append(string[i])
i=0
for i in range(0,l):
    print(n[i],end='')
