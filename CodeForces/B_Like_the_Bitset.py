for _ in range(int(input())):
    n,k=map(int,input().split())
    s = str(input())
    ls = list(map(int,s))
    new=[0]*n
    count=0
    Flag = True
    for x in ls:
        if x == 1:
            count += 1
        else:
            if count >= k:
                Flag = False
                break
            else:
                count = 0
    if count >= k:
        Flag = False
    if(Flag==False):
        print("NO",end="\n")
    else:
        c=1
        d=n
        for i in range(n):
            if ls[i]==1:
                new[i]=c
                c+=1
            else:
                new[i]=d
                d-=1
        print("YES",end="\n")
        for x in new:
            print(x,end=" ")
        print()
                
        
