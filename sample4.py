# class and objects

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def showDetails(self):
#         details="I am {}, {} years old"
#         print(details.format(self.name,self.age))

# p1=person("benin",21)
# p1.showDetails()    

# class student(person):
#     def __init__(self, name, age,SSLC,HSC,college):
#         self.SSLC=SSLC
#         self.HSC=HSC
#         self.college=college
#         super().__init__(name, age)

#     def showDetails(self):
#         super().showDetails() 
#         eduDetails="SSLC: {} , HSC: {} , College: {}"
#         print(eduDetails.format(self.SSLC,self.HSC,self.college))
        
# s1=student("benin",21,"GOVT.VHSS,PARASSALA","LMS HSS,AMARAVILA","MCET,ATTOOR")  
# s1.showDetails()  

       