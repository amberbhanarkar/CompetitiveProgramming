T = int(input())
lis = []
def rec_angry_stu(string, num):
    k =1
    cnt = 0
    for i in range(2,num):
        if string[i]=='P' and string[k]=='A':
            cnt = cnt+1
            k = i
    return cnt
for i in range(0,T):
    k = int(input())
    s = list(map(str, input().split()))
    a = rec_angry_stu(s, k)
    print(a)
    
