for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    a_2 = c-a
    b_2 = d-b
    if a<=b:
        pos = a*2+2
        if(b<=pos):
            if(a_2<=b_2):
                pos_2=a_2*2+2
                if(b_2<=pos_2):
                    print("YES")
                else:
                    print("NO")
            else:
                pos_2=b_2*2+2
                if(a_2<=pos_2):
                    print("YES")
                else:
                    print("NO")
        else:
            print("NO")
    else:
        pos = b*2+2
        if(a<=pos):
            if(a_2<=b_2):
                pos_2=a_2*2+2
                if(b_2<=pos_2):
                    print("YES")
                else:
                    print("NO")
            else:
                pos_2=b_2*2+2
                if(a_2<=pos_2):
                    print("YES")
                else:
                    print("NO")
        else:
            print("NO")