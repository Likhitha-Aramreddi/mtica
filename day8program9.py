def checkEvenOdd(num1):
    assert(num1>0),"Negative Numbers"
    if num%2==0:
        return "Even"
    else:
        return "Odd"
for i in range(5):
    num=int(input("Enter a no:"))
    try:
        print(num,"is",checkEvenOdd(num))
    except AssertionError as ob:
        print(ob)
