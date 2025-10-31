n,m,a,b = map(int,input().split())
if m > n and a*n>b:
    print(b)
else:
    noncombo=a*m
    if noncombo<b:
        print(n*a)
    else:
        com=n%m
        #print(com)
        one=((com)*a)+(((n-com)//m)*b)
        sec=(((n-com)//m)*b)+b
        # print(sec)
        print(min(one,sec))