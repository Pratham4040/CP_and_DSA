for _ in range(int(input())):
    n = int(input())
    s = str(input())
    a=[]
    b=[]
    for i in range(1,n+1):
        if s[i-1] =='a':
            a.append(i)
        else:
            b.append(i)
    if len(a)==0 or len(b)==0:
        print(0)
    else:
        val_a,val_b=0,0
        if len(a)==0:
            val_a=0
        else:
            mid = int(len(a)/2)
            for i in range(len(a)):
                val_a+=abs(a[mid] - a[i])-abs(mid-i)
                #print(a,val_a,mid)
        if len(b)==0:
            val_b=0
        else:
            mid2 = int(len(b)/2)
            for i in range(len(b)):
                val_b+=abs(b[mid2]-b[i])-abs(mid2-i)
        print(min(val_a,val_b))