class Student:

    def setName(self,name):
        self.__name=name

    def getName(self):
        return self.__name
    
    def setRollNumber(self,rollNumber):
        self.__rollNumber=rollNumber
    
    def getRollNumber(self):
        return self.__rollNumber

student1=Student()
student1.setName('surya')
student1.setRollNumber(170)
print(student1.getName())
print(student1.getRollNumber())