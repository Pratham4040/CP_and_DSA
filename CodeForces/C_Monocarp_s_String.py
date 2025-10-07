for _ in range(int(input())):
    n = int(input())
    s = str(input())
    a = s.count('a')
    b = s.count('b')
    if a == b:
        print(0)
    elif a == 0 or b ==0:
        print(-1)
    else:
        pairs=1
        p={}
        for i in range(1,n):
            if s[i]==s[i-1]:
                pairs+=1
            else:
                p.setdefault(s[i-1],[]).append(pairs)
                pairs=1
        p.setdefault(s[-1],[]).append(pairs)
        #print(p)
        if a>b:
            if max(p['a'])>=a-b:
                print(a-b)
            else:
                print(-1)
        else:
            if max(p['b'])>=b-a:
                print(b-a)
            else:
                print(-1)