def count_specialcharacter(s):
    specialcharacter=0
    for i in s:
        #print("i=",i)
        if i not in 'ABCDR=EFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789':
            #temp_specialcharacter+=i
            #print("i:",i,"temp_specialcharacter:",temp_specialcharacter)
            specialcharacter+=1
    return specialcharacter
str1=input()
a=count_specialcharacter(str1)
print("no specialcharacter in:'",str1,"'is",a)
