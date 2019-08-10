n=int(input())
p=0
for i in range(1,8,1):
    if(n%i==0):
       p=p+1
if(p==2):
    print("yes")
else:
    print("no")
