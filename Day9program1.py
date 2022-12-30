##def printSeriesIncreasing(ch,n):
## for i in range(1,n+1,1):
##   print(ch*i)
##   return None
def printSeriesDecreasing(ch,n):
 assert isinstance(ch,str),'first argument to be string'
 assert isinstance(n,int),'second argument to be string'
 for i in range(n,0,-1):
   print(ch*i)
 return None

inpch=input("enter no of character")
inpNum=int(input("enter a no:"))
print('-'*40)
try:
 printSeriesDecreasing(inpch,inpNum)
except AssertionError as obj:
    print(obj)
