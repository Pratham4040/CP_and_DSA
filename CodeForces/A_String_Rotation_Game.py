for _ in range(int(input())):
    n = int(input())
    s = str(input())
    cnt=0
    for i in range(1,len(s)):
        if s[i] != s[i-1]:
            cnt+=1
    ans =cnt+1
    for i in range(1,len(s)+1):
        cnt=0
        for x in range(1,len(s)):
            if s[(x+i)%n] != s[(x+i-1)%n]:
                cnt+=1
        ans= max(ans,cnt+1)
    print(ans)