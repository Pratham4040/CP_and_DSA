from bisect import bisect_right
for _ in range(int(input())):
    n,a = map(int,input().split())
    l = list(map(int,input().split()))
    le=0
    gr=0
    for x in l:
        if x <= a:
            le+=1
        if x >=a:
            gr+=1
    # print(le,gr)
    if le > gr:
        print(a-1)
    else:
        print(a+1)