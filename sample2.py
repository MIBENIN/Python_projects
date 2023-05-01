# List

# mylist=["apple"]
# myList=["apple","orange"]
# print(mylist,myList)

# myLIST=list(("apple","watermelon","guava","apple","watermelon","guava"))
# print(myLIST)
# print(len(myLIST))
# print(type(mylist))

# print("List:ordered,changeable,allow duplicates")

# print(myLIST[1]) #watermelon

# thisList=["bike","car","lorry","aeroplane","helicopter"]
# thisList[1]="bicycle"
# print(thisList) #['bike', 'bicycle', 'lorry', 'aeroplane', 'helicopter']
# thisList[1:3]=["bike","bicycle"]
# print(thisList) #['bike', 'bike', 'bicycle', 'aeroplane', 'helicopter']

# thisLIST=[]
# thisLIST.append("apple")
# print(thisLIST) #['apple']

# thisLIST.insert(1,"orange")
# print(thisLIST) #['apple', 'orange']

# thisLIST[2]="guava"
# print(thisLIST) #IndexError: list assignment index out of range

# thislist=["watermelon","blueberry","strawberry"]
# thisLIST.extend(thislist)
# print(thisLIST) #['apple', 'orange', 'watermelon', 'blueberry', 'strawberry']

# thisLIST.pop(2)
# print(thisLIST) #['apple', 'orange', 'blueberry', 'strawberry']

# thisLIST.remove("apple")
# print(thisLIST) #['orange', 'blueberry', 'strawberry']

# thislist.clear()
# print(thislist) #[]

# del thisLIST[0]
# print(thisLIST) #['blueberry', 'strawberry']

# del thisLIST
# print(thisLIST) #NameError: name 'thisLIST' is not defined

# LIST=["APPLE","BANANA","DRAGON FRUIT","SAPPOTTA","GRAPES"]
# for x in LIST:
#     print(x)

# for i in range(len(LIST)):
#     print(LIST[i])   #APPLE
#                      #BANANA
#                      #DRAGON FRUIT
#                      #SAPPOTTA
#                      #GRAPES

# LIST.sort()
# print(LIST) #['APPLE', 'BANANA', 'DRAGON FRUIT', 'GRAPES', 'SAPPOTTA']

# LIST.sort(reverse=True)
# print(LIST) #['SAPPOTTA', 'GRAPES', 'DRAGON FRUIT', 'BANANA', 'APPLE']

# list1=["apple"]
# list2=["orange","guava"]
# list3=list1 + list2
# print(list3) #['apple', 'orange', 'guava']

# for x in list2:
#     list1.append(list2)
#     print(list1) #['apple', ['orange', 'guava'], ['orange', 'guava']]

# tuple

# print("Tuple : unchangeable ordered and allow duplicates")

# myTUPLE=tuple(("apple","234",12,"fcc is awesome"))
# print(myTUPLE) #('apple', '234', 12, 'fcc is awesome')
# print(type(myTUPLE)) #<class 'tuple'>
# print(len(myTUPLE)) #4

# to add items to tuple

# convert tuple to list

# mytuplelist=list(myTUPLE)
# mytuplelist.append("orange")
# print(mytuplelist) #['apple', '234', 12, 'fcc is awesome', 'orange']

# my_Tuple_1=("vijay",)
# my_Tuple_2=("surya",)
# my_Tuple_1+=my_Tuple_2
# print(my_Tuple_1) #('vijay', 'surya')

# MyTuple=("vijay sethupathi")
# print(MyTuple)

actors=("surya","dhanush","vikram")
x,y,z=actors
print(x)
print(y)
print(z)