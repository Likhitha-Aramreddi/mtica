fo=open(r"D:\pythonpractice30\Day10\abcde.txt","+w")
for i in range(5):
    inpstr=input("Enter String:")
    fo.write(inpstr+'\n')
fo.close()
print("written to file")
