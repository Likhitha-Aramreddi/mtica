import math
def checkprimeNumber(num):
    if num<1:
        return 0
    if num==1 or num==2 or num==3:
        return num
    count=int(math.sqrt(num))+1
    for i in range(2,count):
        if num%i==0:
            return 0
    return num
start=int(input())
stop=int(input())
lst=[]
for i in range(start,stop+1):
        if checkprimeNumber(i):
           lst.append(i)
print(*lst)
print(len(lst))          
