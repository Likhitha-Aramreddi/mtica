##class A:
##    def first_method(self):
##        print("Method of class A...")
##class B(A):
##    def second_method(self):
##        print("Method of class B...")
##class C(B):
##    def third_method(self):
##        print("Method of class c..")
##if __name__=='__main__':
##    ob=C()
##    ob.first_method()
##    ob.second_method()
##    ob.third_method()
##    C().third_method()

class A:
    def first_method(self):
        print("Method of class A...")
class B:
    def first_method(self):
        print("Method of class B...")
class C(B,A):
    def third_method(self):
        print("Method of class c..")
if __name__=='__main__':
    ob=C()
    ob.first_method()
##    ob.second_method()
    ob.third_method()
##    C().third_method()
