# if 5 > 2:
#  print("Five is greater than two!")  
# if 5 > 2:
#  print("Five is greater than two!")

# a=5
# b="bear"
# print(a+b) #TypeError: unsupported operand type(s) for +: 'int' and 'str'

# a=int(8.0)
# b=float(2)
# c=float("7")
# d=str(678)
# e=str(457.98)
# f=int(345.6)
# g=int("349")
# print(a ,b,c,d,e,f,g) #8 2.0 7.0 678 457.98 345 349

# mylist=["apple","orange"]
# print(type(mylist))  #<class 'list'>

# x,y,z="orange","apple"
# print(x)
# print(y)
# print(z) #ValueError: not enough values to unpack

# x,y,z="orange","apple","guava"
# print(x)  #orange
# print(y)  #apple
# print(z)  #guava

# x=y=z="orange"
# print(x) #orange
# print(y) #orange
# print(z) #orange

# print("Data types in Python: int,float,complex,str,list,tuple,range,dict,set,frozenset,bool,bytes,bytesarray,memoryview,noneType")

# x=int(3)
# x=3 #both are same

# import random
# print(random.randrange(1,10))  #random number using random module

# multiline string
# stR=""" lopem ipsum lorem isum
# lopem ipsum lorem isum
# lopem ipsum lorem isum. """
# sTr='''lopem ipsum lorem isum
# lopem ipsum lorem isum
# lopem ipsum lorem isum '''

# print(stR)
# print(sTr)

# hel="hello, World!"
# hel[1]="W"
# print(hel) #TypeError: 'str' object does not support item assignment

# hel="hello world"
# for x in hel:
#     print(x)

# he="hello world"
# if "h" in  he:
#     print("H is present")
# else:
#     print("h not present")     

# he="hello world"
# if "i" not in  he:
#     print("i not present") #i not present
# else:
#     print("i present")   

# name="benin s"
# print(len(name)) #7

# name="benin s"
# print(name.replace("b","l")) #lenin s

# name="benin"
# print(name.upper())  #BENIN

# name="benin"
# print(name.capitalize()) #Benin

# name="BENIN"
# print(name.casefold())  #benin

# name="BENIN"
# print(name.lower()) #benin

# name="benin"
# print(name.title())  #Benin

# p="this is a paragraph.this is a paragraph.this is a paragraph.this is a paragraph."
# print(p.count("this"))  #4

# p="this is a paragraph.this is a paragraph."
# print(p.find("is")) #2

# p="this is a paragraph. this is a paragraph."
# print(p.index("is")) #2

# age=36
# text="i am {} years old"
# print(text.format(age))

# mystr=" "
# myList=["apple","orange"]
# print(mystr.join(myList))

# print(bool(""))
# print(bool([]))
# print(bool(()))
# print(bool({}))
# print(bool(None))
# print(bool(False))
# print(bool(0)) #all gives false

print("operators in python : arithmetic,assignment,logical,identity,membership,comparison,bitwise")