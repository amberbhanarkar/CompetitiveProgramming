#Activity selection problem
print("Enter number of activities: ")
num = int(input())
star = []
fin = []
lis = []
print("Enter start time and finish time of activities: ")
def rec_act_sel(star, fin, num):
    i= 2 
    k = 1
    for i in range(2,num):
        if star[i]>=fin[k]:
            lis.append(i)
            k = i
        i=i+1
    return lis
for i in range(0,num):
    start, finish = map(int,input().split())
    star.append(start)
    fin.append(finish)
    #fin = sorted(fin)
    #star = sorted(star)
#print(fin)
#print(star)
a = rec_act_sel(star, fin, num)
print(a)
