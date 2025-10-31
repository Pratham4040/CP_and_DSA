import math
for _ in range(int(input())):
    n,k=map(int,input().split())
    x = k + (k-1)//(n-1)
    print(x)