# thisSet={"apple","banana"}
# print(thisSet) #{'apple', 'banana'}
# print(type(thisSet)) #<class 'set'>
# print(len(thisSet)) #2

# mySet=set(("guava","green apple","blue berry"))
# print(mySet) #{'guava', 'green apple', 'blue berry'}

# print("NB:set - unordered,duplicates not allowed, unchangeable")
# print("NB: Can't able to access set by index ")

# set1={1,2,3,4}
# set2={1,2,4,5} 
# print(set2) #{1, 2, 4, 5}
# set1.add(6)
# print(set1) #{1, 2, 3, 4, 6}
# set2.update(set1)
# print(set2) #{1, 2, 3, 4, 5, 6}

# set4={5,6,7,8}
# set5={7,5,8,9,2,4}
# print(set4.union(set5)) #{2, 4, 5, 6, 7, 8, 9}

# print(set4.intersection(set5)) #{8, 5, 7}
# print(set5.difference(set4)) #{9, 2, 4}
# print(set5.symmetric_difference(set4)) #{2, 4, 6, 9}
# print(set4.difference_update(set5)) #None

# Functions

# default parameter

# def myFunc(name="benin"):
#     print("My name is " + name)

# myFunc()
# myFunc("sneha")   

# keyword parameter

# def myFn(brother,sister):
#     print("Brother:" + brother)
#     print("Sister:" + sister)
# myFn(brother="benin",sister="sneha")     

# arbituary keyword parameter

# def myData(**keys):
#     print("The first child is :"+keys["child1"])

# myData(child1="benin",child2="sneha")

# arbituary parameter

# def func(*keys):
#     print("The first name is : " + keys[0])
#     print("The middle name is : " + keys[1])
#     print("The last name is : " + keys[2])
# func("Benin","S","Steephen")  

# sum=lambda a,b:a+b
# print(sum(5,3))  

# comp=lambda a,b:print(a) if a>b else print(b)
# print(comp(9,4))


