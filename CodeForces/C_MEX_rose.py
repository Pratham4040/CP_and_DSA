for _ in range(int(input())):
    n,k = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    d = {}
    c=0
    for x in A:
        d[x] = d.get(x,0)+1
    for i in range(0,k):
        if i not in d:
            #print(1)
            c+=1
    print(max(c,d.get(k,0)))
    # i=0
    # mex=max(A)+1
    # for x in A:
    #     if x!=i:
    #         mex=i
    #         break
    #     i+=1
    # if mex == k:
    #     print(0)
    # else:
    #     i=0
    #     c = 0
    #     for x in A:
    #         if i < k or x ==k:
    #             #print("h")
    #             if x!=i or x == k:
    #                 c+=1
    #         i+=1
    #     #print(A[mex:k])
    #     if (k in A):
    #         idx = A.index(k)
    #     else:
    #         idx = mex
    #     new = set(A[mex:idx])
    #     print(c-len(new))