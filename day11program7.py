##employees=['Likhi','ramu','manu']
##defaults={"designation":'Developer',"salary":80000}
##data=dict()
##for i in employees:
##    data[i]=defaults
##print(data)    


employees=['Likhi','ramu','manu']
defaults={"designation":'Developer',"salary":80000}
data= dict.fromkeys(employees,defaults)
print(data)
print(data["ramu"])
