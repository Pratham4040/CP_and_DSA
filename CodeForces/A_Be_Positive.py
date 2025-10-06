for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    z=A.count(0)
    p=A.count(1)
    n=A.count(-1)
    count = z
    if n %2 !=0:
        count+=2
    print(count)