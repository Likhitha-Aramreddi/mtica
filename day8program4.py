num1 =int(input("Enter a number"))
num2=int(input("Enter a nuimber"))
try:
    res=num1/num2 #Excute with num2=non zero and zero
except ZeroDivisionError:
    print("Division by zero not allowed")
else:
    print(num1, '/' ,num2, '=', res)
    print('thanks')
