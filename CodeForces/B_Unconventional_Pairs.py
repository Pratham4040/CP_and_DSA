for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    A.sort()
    x=0
    sumi=[]
    while x<n:
        sumi.append(abs(A[x]-A[x+1]))
        x+=2
    print(max(sumi))