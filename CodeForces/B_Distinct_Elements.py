for _ in range(int(input())):
    n = int(input())
    L = list(map(int,input().split()))
    ans=[n]*n
    p=n
    for i in range(1,n):
        diff = (L[i]-L[i-1]-1)
        #print(diff)
        if diff == i:
            p=p-1
            ans[i]=(p)
        else:
            ans[i]=(ans[i-diff-1])
    for x in ans:
        print(x,end=" ")
    print()