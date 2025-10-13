for _ in range(int(input())):
    n = int(input())
    L = list(map(int,input().split()))
    s = set(L)
    mex = 0
    while mex in s:
        mex += 1
    print(mex)