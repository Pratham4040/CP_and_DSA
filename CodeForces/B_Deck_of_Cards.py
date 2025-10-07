for _ in range(int(input())):
    n,k = map(int,input().split())
    s = list(input())
    if n==k:
        ans=""
        for _ in range(n):
            ans+="-"
        print(ans)
        continue
    f,e=[],[]
    c2=0
    for x in s:
        if x=="0":
            f.append("-")
        elif x == "1":
            e.append("-")
        else:
            if x == "2":
                c2+=1
    ans=["+"]*(n-(len(f)+len(e)))
    for i in range(c2):
        ans[i]="?"
        ans[-(i+1)]="?"
    print("".join(f+ans+e))    