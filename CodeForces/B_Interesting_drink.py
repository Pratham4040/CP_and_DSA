n = int(input())
C = list(map(int,input().split()))
q = int(input())
C.sort()
for _ in range(q):
    x = int(input())
    l=0
    h=n-1
    ans=0
    while l <= h:
        mid = l+(h-l)//2
        if C[mid]<=x:
            l=mid+1
            ans=mid+1
        elif C[mid]>x:
            h=mid-1
    print(ans)