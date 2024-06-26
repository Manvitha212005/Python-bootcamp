DAY4BOOTCAMP
"""
INHERITANCE"""
class A:
    var1=10
    def test(self):
        print("i am in A")
class B:
    var2=5010
    def run(self):
        print("i am running")
a1=A()
a2=B()
#MULTILEVEL
 class A:
     class B(A):
         class C(B):
             #MULTIPLE
             2PARENT 1 CHILD
             #CODE
             class A:
                 class B:
                     class C(A,B):
                         #A AND b have diff then okay if same fun name first it will go A then stop
                         #method resolution order
                         c.mro()
                         #DECORATION
                         take a fn change and return fn

