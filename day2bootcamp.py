"""
#day 2 bootcamp
module=any python file with(.py)
predefined
example:
    def greet()
    print("hello welcome")
packages: collection of modules
syntax:
    __init__.py(empty file)
package is a folder with many files
we import only modules not packages
if two modules are not in  same path(error)
we have to set a absolute(from directory) path
"""
"""
a=10
def greet():
    print("hello world")
f2.py
import f1
f1.test1
f1 not found because diff dir we should set path """
"""
import os
import sys
module_path=os.path.abspath(os.path.join("..\p1")
                            sys.path.append(module_path)
                            import f1
                            f1.test
                            ------------------------
                            library=collection of modules and packages
                            csv=, seperated values
                            in an excel sheet you can convert it manually
    """
"""\
file hsndlings
open()-filename and mode
"t"-text
"b"-binary
"r"-read
"w"-write
"a"-append
"x"-write
syntax
f=open("file.txt")
returns file objects
read()-read the content
we should close the files
to write,add parameter to open()
os.remove()-remove file
os.rmdir()-remove folder
"""
"""
#homework
f=open("C:\\Users\\manvitha\\Desktop\\Python\day2fil.txt","r")
print(f.read())
"""
"""
csv basics
f=open("student.csv","r")
headers=next(csvreader)
csvreader=csv.reader(f)
for i in csvreader:
    print(i)
    """

