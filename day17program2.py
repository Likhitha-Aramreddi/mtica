import  sys
print("coming through stdout")
save_stdout=sys.stdout
fh=open(r"D:\python.28\day17\likhi.txt","w")
sys.stdout=fh
print("This line goes to likhi.txt")
print(input())
sys.stdout=save_stdout
fh.close()      
      
