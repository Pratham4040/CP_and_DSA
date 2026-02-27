def factor(n,k):
    ans= 1
    for i in range(int(n**0.5),1,-1):
       if n%i == 0:
            s1 = i
            s2 = n//i
            if s1 <= k:
               ans =  max(s1,ans)
            if s2 <= k:
                ans = max(s2,ans)
    return ans
for _ in range(int(input())):
    n,k = map(int,input().split())
    if k >= n:
        print(1)
    elif k == 1:
        print(n)
    else:
        #print(factor(n,k))
        print(n//factor(n,k))