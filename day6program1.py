lst=[]
while(True):
 inpNum=int(input("enter a value(0 to end):"))
 if inpNum==0:
    break
 else:
    lst.append(inpNum)
lst.sort()   
print("Min:",lst[0])
print("Max:",lst[-1])
print("Avg:",round(sum(lst)/len(lst),1))
