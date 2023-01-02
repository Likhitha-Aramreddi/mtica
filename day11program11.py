sample_dict={
    "name":"Kelly",
    "age":25,
    "salary":8000,
    "city":"Newyork"}
sample_dict["location"]=sample_dict.pop("city")
print(sample_dict)
