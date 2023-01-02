sample_dict={
    "name":"Kelly",
    "age":25,
    "salary":8000,
    "city":"Newyork"}
keys=["name","salary"]
newDict={}
for i in keys:
   newDict[i]=sample_dict[i]
print(newDict)

newDict={k:sample_dict[k] for k in keys}
print(newDict)

res=dict()
for k in keys:
    res.update({k:sample_dict[k]})
print(res)    

