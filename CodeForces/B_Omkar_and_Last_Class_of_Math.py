import math 
for _ in range(int(input())):
    flag=False
    n = int(input())
    if n%2 ==0:
        flag=True
        print(int(n/2),int(n/2))
    else:
        for i in range(3,int(n**0.5)+1,2):
            if n%i==0:
                a=n//i
                b=n-a
                print(a,b)
                flag=True
                break
    if flag == False:
        print(1,n-1)