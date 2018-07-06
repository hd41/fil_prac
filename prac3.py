# lis  = [5,9,4,2,0,8,4,6,3,7,5,0,1,2,8,4,1,7,3,6,5,1]
def naive_approach(total,lis):
    flag,sum=0,0
    tmp =0
    for i in (lis):
        if i==2:
            tmp=0
            flag=1
        elif i==3:
            tmp +=3
            sum+=tmp
            flag=0
        if flag==1:
            tmp+=i
    print (total-sum)

lis=[]
inp = int(input("Enter no. of items: "))
total = 0
for i in range(inp):
    tmp = int(input("Enter no. "+str(i+1)+" : "))
    total+=tmp
    lis.append(tmp)

naive_approach(total,lis)
