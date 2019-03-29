l=[];
n=int(input());
for i in range(0,n):
    m=[];
    for j in range(0,n):
        x=int(input());
        m.append(x);
    l.append(m);
a=(8*n)-12;
i=0;
j=0;

if (n%2)==0:
    for j in range(0,n-2,2):
        l[i][j],l[i][j+2]=l[i][j+2],l[i][j]
    j=n-2;
    l[i][j],l[i+1][j+1]=l[i+1][j+1],l[i][j];
    i=0; j=n-1;
       
    
    for i in range(1,n-2,2):
        l[i][j],l[i+2][j]=l[i+2][j],l[i][j];
         
    i=i+2;
    i=n-1; j=n-1; 
    
    for j in range(n-1,2,-2):
        l[i][j],l[i][j-2]=l[i][j-2],l[i][j]
    j=j-2;
    l[i][j],l[i-1][j-1]=l[i-1][j-1],l[i][j];
    i=n-1; j=0;
    
    for i in range(n-2,2,-2):
        l[i][j],l[i-2][j]=l[i-2][j],l[i][j];



else:
    for j in range(0,n-1,2):
        l[i][j],l[i][j+2]=l[i][j+2],l[i][j]
    i=0; j=n-1;
       
    
    for i in range(0,n-1,2):
        l[i][j],l[i+2][j]=l[i+2][j],l[i][j];
         
   
    i=n-1; j=n-1; 
    
    for j in range(n-1,0,-2):
        l[i][j],l[i][j-2]=l[i][j-2],l[i][j]
    
    i=n-1; j=0;
    
    for i in range(n-1,2,-2):
        l[i][j],l[i-2][j]=l[i-2][j],l[i][j];




for i in range (0,n):
    for j in range(0,n):
        print(l[i][j],'\t',end='')
    print('')
