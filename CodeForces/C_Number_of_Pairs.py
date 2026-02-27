import bisect
for _ in range(int(input())):
    n,l,r = map(int,input().split())
    li= list(map(int,input().split()))
    li.sort()
    ans=0
    #print(li)
    for i in range(n):
        one = bisect.bisect_left(li,l-li[i],i+1)
        two = bisect.bisect_right(li,r-li[i],i+1)
        #print(one,two)
        ans += two-one 
    print(ans)
    