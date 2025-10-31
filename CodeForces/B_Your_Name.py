for _ in range(int(input())):
    n = int(input())
    a,b = map(str,input().split())
    if sorted(a) == sorted(b):
        print("YES")
    else:
        print("NO")