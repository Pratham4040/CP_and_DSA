for _ in range(int(input())):
    x = int(input())
    a = -360/(x-180)
    if (int(a)-a)==0:
        print("YES")
    else:
        print("NO")