student=[[30,'likhitha',80,75],[12,'sai',78,82],[44,'ramu',72,89],[29,'lakshmi',79,84]]
student.sort()
print(student)
student.sort(key=lambda temp:temp[2])
print(student)
student.sort(key=lambda temp:temp[1])
print(student)
