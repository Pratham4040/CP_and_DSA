t = int(input())
for _ in range(t):
    n = int(input())
    a = str(input())
    m = int(input())
    b = str(input())
    c = str(input())
    back =""
    front = ""
    for i in range(m):
        if c[i] == 'V':
            front += b[i]
        elif c[i] == 'D':
            back += b[i]
    ans = front[::-1]+a+back
    print(ans)