for _ in range(int(input())):
    s = str(input())
    cnt1=0
    cnt2=0
    flag=False
    for i in range(1,len(s)):
        if s[i]==s[i-1] and s[i]==">":
            cnt1+=1
        elif s[i]==s[i-1] and s[i]=="<":
            cnt2+=1
        elif s[i]==s[i-1] and s[i]=="*":
            flag=True
            break
        else:
            if s[i-1]==">" and s[i]=="*":
                flag = True
                break
            elif s[i-1]=="<" and s[i]=="*":
                cnt2+=1
            elif s[i-1]=="*" and s[i]==">":
                cnt1+=1
            elif s[i-1]==">" and s[i]=="<":
                flag = True
                break
            elif s[i-1]=="*" and s[i]=="<":
                flag = True
                break
            elif s[i-1]=="<" and s[i]==">":
                pass
    if flag:
        print(-1)
    else:
        print(max(cnt1+1,cnt2+1))