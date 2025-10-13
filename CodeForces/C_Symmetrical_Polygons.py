from random import getrandbits
RD = getrandbits(31)
for _ in range(int(input())):
    n = int(input())
    S=list(map(int,input().split()))
    if n ==3:
        sumi=sum(S)
        done=False
        for x in S:
            if (sumi-x)<=x:
                done=True
        if (done):
            print(0)
        else:
            if (len(set(S))!=3):
                print(sumi)
            else:
                print(0)
    else:
        cnt=0
        di={}
        sumi=sum(S)
        lef=[]
        half=0
        for x in S: 
            di[x^RD]=di.get((x^RD),0)+1
        for x in di.keys():
            if di[x]>1:
                cnt+=di[x]//2
                half+=(di[x]//2)*(x^RD)
            if(di[x]%2==1):
                lef.append(x^RD)
        #print(di)
        #print(cnt)
        #print(half)
        lef.sort()
        ans=0
        if cnt<=1:
            ans=0
        else:
            ans=half*2
        #print(ans)
        for x in lef:
            if half*2>x:
                ans=max(ans,(half*2)+x)
        #print(ans)
        for i in range(1,len(lef)):
            if half *2 >lef[i]-lef[i-1]:
                ans=max(ans,(half*2)+(lef[i]+lef[i-1]))
        print(ans)