def printDay(dn):
 if(dn==1):
   da= "monday"
 elif(dn==2):
   da= "tuesday"
 elif(dn==3):
   da= "wednesday"
 elif(dn==4):
   da= "thursday"
 elif(dn==5):
   da= "friday"
 elif(dn==6):
  da= "saturday"
 return da
def printDay1(dn):
 if(dn==1):
   da= "monday"
 if(dn==2):
   da= "tuesday"
 if(dn==3):
   da= "wednesday"
 if(dn==4):
   da= "thursday"
 if(dn==5):
   da= "friday"
 if(dn==6):
  da= "saturday"
 return da

import time     
for i in range(3):
    inpNum=int(input())
    start=time.time()
    print(printDay(inpNum))
    print((time.time()-start)*100000)
    strat=time.time()
    print(printDay1(inpNum))
    print((time.time()-start)*100000)

    
