for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ind=l.index(max(l))
    l[ind],l[0]=l[0],l[ind]
    for x in l:
        print(x,end=" ")
    print()