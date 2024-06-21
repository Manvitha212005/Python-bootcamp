"""
array:only single data type
list:different data type
methods:
    a=[1,2,3,4,5]
    a.append(8)
    a.insert(index,number)
    a.pop(index)
    a.remove(number)
    a.sort()
    a[start:end:direction]
    x=list(map(int,input().split(" ")))
    map converts all data types in one group
    converts list of strings to a list of numbers
    it will accept 2 parametrs
    map(int,input.split(" ")
        tuples:
        immutable,ordered
        when you use constants
        ,- to define tuples
        in-check weather it is present or not
        sets:
        unorderd,duplicate
        s={} considerd as dictionary
        s=set{} considered as set data type
        dictionary has key and pair
        sets are mutable but values in it are immutable
        """


"""
input a sentence and print only those words whose length is >2
"""
"""
#code
t=[]
s=input().split()
for i in s:
    if len(i)>2:
        t.append(i)
print(t)
"""
"""
def unique(lst:list[str]):
    s=[]
    for x in lst:
        if lst.count(x):
            if lst.count(x)==1:
                s.append(x)
            else:
                return(x)
        return s
"""


