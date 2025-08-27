from math import gcd
for _ in range(int(input())):
    n,k = map(int,input().split())
    num = list(map(int,input().split()))
    if  n == 1:
        if num[0]==1:
            print(num[0]+k,end=" ")
            print()
        else:
            print(num[0],end=" ")
            print()
    else:
        if k%2 !=0:
            for x in num:
                if x%2 !=0:
                   print (x+k,end=" ")
                else:
                    print(x,end=" ")
            print()
        else:
            i=k
            while gcd(k,i) != 1:
                i+=1
            off = k%i
            print(off)
            for x in num:
                off2 = i%x
                
                times = (x%i)
                print (x+k*times,end = " ")
            print()