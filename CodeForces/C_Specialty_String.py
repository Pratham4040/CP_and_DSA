from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = str(input())
    st=[]
    for i in range(len(s)):
        if len(st)==0:
            st.append(s[i])
        elif s[i]==st[-1]:
            st.pop()
        else:
            st.append(s[i])
    if len(st)==0:
        print("YES")
    else:
        print("NO")