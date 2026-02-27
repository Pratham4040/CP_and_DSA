for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ind=l.index(max(l))
    for i in range(1,n):
        #print(l[:i])
        mx = max(l[:i])
        #print(mx)
        indx = l.index(mx)
        #print(i,mx)
        #print(l)
        if mx == i:
            l[ind],l[indx]=l[indx],l[ind]
            break
        #print(l)
    for x in l:
        print(x,end=" ")
    print()