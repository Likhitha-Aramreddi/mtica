def printMonth(dn):
 if(dn==1):
   return "Januvary"
 if(dn==2):
   return "Feb"
 if(dn==3):
   return "march"
 if(dn==4):
   return "April"
 if(dn==5):
   return "may"
 if(dn==6):
     return "june"
 if(dn==7):
    return "july"
 if(dn==8):
    return "Augus"
 if(dn==9):
    return "sep"
 if(dn==10):
    return "oct"
 if(dn==11):
    return "nov"
 if(dn==12):
    return "dec"
 else:
   return "Invalid"
      
for i in range(3):
    inpNum=int(input())
    print(printMonth(inpNum))
