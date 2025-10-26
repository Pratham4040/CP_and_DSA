n,k = map(int,input().split())
H = list(map(int,input().split()))
if k ==1 :
    print(H.index(min(H))+1)
else:
    curr = sum(H[:k])
    #print(curr)
    mins = curr
    ans=0
    for i in range(k,n):
        curr = (mins-H[i-k])+H[i]
        #print(curr)
        if curr < mins:
            mins=curr
            ans = i-k+1
    print(ans+1)