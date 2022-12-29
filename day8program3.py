def div(a,b):
    assert( isinstance(a,int) or isinstance(a,float)), \
              'First Argument should be either integer or float'
    assert( isinstance(b,int) or isinstance(b,float)), \
              'Second Argument should be either integer or float'
    assert (b!=0),"Division by Zero is not defined"
    return a/b
try:
    print(div(55,0))
except AssertionError as obj:
    print(obj)
try:
    print(div(20,3))
except AssertionError as obj:
    print(obj)
try:
    print(div('helo',20))
except AssertionError as obj:
    print(obj)
try:
    print(div(20,'helo',))
except AssertionError as obj:
    print(obj)    
    
print('thank youuuu')
