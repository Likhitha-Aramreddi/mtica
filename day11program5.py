##dic1={'Ten':10,'Twenty':20,'Thirty':30}
##dic2={'Thirty':30,'Fourty':40,'Fifty':50}
##dic3={**dic1,**dic2}
##print(dic3) 
##
dict1={'Ten':10,'Twenty':20,'Thirty':30}
dict2={'Thirty':30,'Fourty':40,'Fifty':50}
dict3=dict1.copy()
dict3.update(dict2)
dict3={**dict1,**dict2}
print(dict3)
print(dict3)
