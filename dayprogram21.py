def count_specialcharacter(s):
    n_specialcharacter=0
    for i in s:
        #print("i=",i)
        if i in '@#$%^*_:':
            n_specialcharacter+=1
            #print("i:",i,"temp_vowel:",temp_vowel)
    return n_specialcharacter
str1=input()
a=count_specialcharacter(str1)
print(" no of specialcharacter in:' ",str1," 'is",a)
