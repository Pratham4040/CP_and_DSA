for _ in range(int(input())):
    n,k = map(int,input().split())
    s=""
    r=k
    if k != n*n-1:
        print("YES")
        for i in range(n):
            s=""
            for j in range(n):
                if r>0:
                    s+="U"
                    r-=1
                elif i == n-1 and j == n-1:
                    s+="L"
                elif i == n-1:
                    s+="R"
                else:
                    s+="D"
            print(s)   
    
    else:
        print("NO")
