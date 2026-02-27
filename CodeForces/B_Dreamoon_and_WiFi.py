s1 = str(input())
s2 = str(input())
cnt=0
cnt1=0
q=0
for x in s1:
    if x == "+":
        cnt+=1
    else:
        cnt-=1
for x in s2:
    if x == "+":
        cnt1+=1
    elif x =="-":
        cnt1-=1
    else:
        q+=1
if q ==0:
    if cnt==cnt1:
        print(float(1))
    else:
        print(float(0))
else:
    l=[]
    #print(cnt,cnt1,q)
    for i in range(2**q):
        cnt2=0
        s = bin(i)
        s=s[2:].zfill(q)
        for x in s:
            if x == "0":
                cnt2-=1
            else:
                cnt2+=1
        l.append(cnt2)
    fav=0
    for x in l:
        if x + cnt1 == cnt:
            fav+=1
    #print(fav)
    print((fav)/len(l))
    # print(l)
    # print(s)