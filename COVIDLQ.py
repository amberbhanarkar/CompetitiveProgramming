def check(string, sub_str): 
    if (string.find(sub_str) == -1): 
        return 0
    else: 
        return 1 

T = int(input())
for i in range(0,T):
    N = int(input())
    A = list(map(int,input().split()))
    Str = ''.join(map(str, A))
    #print(Str)
    a = check(Str,'11')
    c = check(Str,'1001')
    d = check(Str,'10001')
    e = check(Str,'100001')
    b = check(Str,'101')
    if a==0:
        if b==0:
            if c==0:
                if d==0:
                    if e==0:
                        print("YES")
                    else:
                        print("NO")
                else:
                    print("NO")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
    '''if Str.find('11') or Str.find('101') or Str.find('1001') or Str.find('10001') or Str.find('100001'):
        return "NO"
    else:
        return "YES"'''
