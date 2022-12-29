num1 =input("Enter a number:")
num2=input("Enter a nuimber:")
try:
    res=int(num1)/int(num2) #Execute with num2=non zero and zero
##except ZeroDivisionError:
##    print("Exception handled by likhitha")
##except ValueError:
##    print("Exception handled by lakshmi")
except (ZeroDivisionError,ValueError):
    print("Exception handled by likhitha")
except Exception as ob:
      print(ob)
else:
    print(num1, '/' ,num2, '=', res)
finally:    
    print('thanks')
print("visit again at python class")    

