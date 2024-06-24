"""
day 3 topup python
text files
"""
"""
f=open("day3.txt","w")
#s=f.readlines()
#s=f.read()
s=["i\am\deepika"]
f.writelines(s)
#writelines independent lines
print(s)"""
"""
#jason file handling
#exactly like a dic
import json
f=open("C:\\Users\\manvitha\\Desktop\\Python\f2.json","r")
#s=json.load(f)
print(f.read())
"""
"""

read a json file which stores a key as student_rollnum and value in dic which stores its name age
create new file whwere ony those students is stores whose age <24"""
"""import json
f=open("f2.json","r")
q=open("f3.json","w")
s=json.load(f)
result={}
for i in s:
    d=s[i]
    if d["age"]<24:#s[i][age]
        result[i]=d
        json.dump(result,q,indent=4)"""
"""
========================================================================
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
========================================================================"""
#OOPS

class Car:
    #color="black"
    #type="electric"
    #milage=250
    def changeValues(self,c,t,m):#constructor
        self.color=c
        self.type=t
        self.milage=m

c1=Car()
c1.changeValues("black","petrol",234)
c2=Car()
c1.color="pink"
print(c1.color)
print(c2.color)
      def __init__(self,c,m)
      #init is a constructur
