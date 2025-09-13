for _ in range(int(input())):
    n,m = map(int,input().split())
    a=[0]*(n+1)
    b=[0]*(n+1)
    count=0
    a[0]=0
    b[0]=0
    for i in range(n):
        a[i+1],b[i+1] = map(int,input().split())
    #print(a,b)
    for i in range(1,n+1):
        diff = a[i]-a[i-1]
        #print(diff)
        if diff%2==0:
            if b[i]==b[i-1]:
                count+=diff
            else:
                count+=diff-1
        else:
            if b[i]!=b[i-1]:
                count+=diff
            else:
                count+=diff-1
    print(count+(m-a[-1]))