for _ in range(int(input())):
    l = list(map(int,input().split()))
    if len(set(l))==1:
        print("YES")
    else:
        print("NO")