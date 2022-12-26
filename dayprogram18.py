def extract_digit(s):
    temp_digit=''
    for i in s:
        print("i=",i)
        if i in '0123456789':
            temp_digit+=i
            print("i:",i,"temp_digit:",temp_digit)
    return temp_digit
str1=input()
a=extract_digit(str1)
print("digit:",a)
