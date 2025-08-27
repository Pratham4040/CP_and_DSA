def solve(n,k,cond):
    ans =0
    if(max(cond)==0):
        return (n // k)
    if(min(cond)==1):
        return 0
    goodays = cond.count(0)   
    baddays = n - goodays
    rest = False    
    for i in range(0,n,1):
        count = 0
        for j in range (i,k+i):
            if(j<n-1):
                if(cond[j]==0):
                    count += 1
        if(count == k and rest == False):
            ans += 1
            rest = True
            i +=k-1
        rest = False    
    return ans     
t=int(input())
for _ in range(t):
    n,k = map(int,input().split())
    cond = list(map(int,input().split()))
    ans =0
    ans = solve(n,k,cond)
    print(ans)