sample_dict={
    "name":"Kelly",
    "age":25,
    "salary":8000,
    "city":"Newyork"}
keys=["name","salary"]
##keys=["age","city"]
##keys=["name"]
for k in keys:
    sample_dict.pop(k)
print(sample_dict)


sample_dict={k:sample_dict[k] for k in sample_dict.keys()-keys}
print(sample_dict)

d=dict()
for i in sample_dict.keys()-keys:
    d[i]=sample_dict[i]
print(d)    
