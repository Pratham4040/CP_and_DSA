s = str(input())
dir = []
cnt2=0
dir.append(0)
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        cnt2+=1
    dir.append(cnt2)
#print(dir)
for i in range(int(input())):
    a,b = map(int,input().split())
    print(dir[b-1]-dir[a-1])