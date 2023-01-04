##def printSunday():
##    print("Sunday")
##def printMonday():
##    print("Monday")
##def printTuesday():
##    print("Tuesday")
##def printWednesday():
##    print("Wednesday")
##def printThursday():
##    print("Thursday")
##def printFriday():
##    print("Friday")
##def printSaturday():
##    print("Saturday")
##def choice():
##    print("0:Sunday")
##    print("1:Monday")
##    print("2:Tuesday")
##    print("3:Wednesday")
##    print("4:Thursday")
##    print("5:Friday")
##    print("6:Saturday")
##    print("7:Quit")
##    return
##colorselect={0:printSunday,1:printMonday,2:printTuesday,3:printWednesday,
##             4:printThursday,5:printFriday,6:printSaturday}
##selection=0
##while True:
##    if selection==7:break
##    choice()
##    selection=int(input("select a day:"))
##    if (selection>=0)and (selection<7):
##        colorselect[selection]()

          

          
def printSunday():
    print("Sunday")
def printMonday():
    print("Monday")
def printTuesday():
    print("Tuesday")
def printWednesday():
    print("Wednesday")
def printThursday():
    print("Thursday")
def printFriday():
    print("Friday")
def printSaturday():
    print("Saturday")
def choose():
    print("Enter day number between 1-7")
dayDict={1:printSunday,2:printMonday,3:printTuesday,4:printWednesday,
         5:printThursday,6:printFriday,7:printSaturday}
choose()
dayNo=int(input())
if dayNo>=0 and dayNo<7:
    dayDict[dayNo]()
else:
    print("invalid")
    
          

          

          
      
          

          

          
      
          
