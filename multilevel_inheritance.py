class Student():
     def getStudentInfo(self):
        self.__rollno=input("Enter Roll Number: ")
        self.__name=input("Enter Name: ")

     def printStudentInfo(self):
        print("Roll Number : ", self.__rollno, "Name : ", self.__name)

class Bsc(Student):
    def getBsc(self):
        self.getStudentInfo()
        self.__p = int(input("Enter Physics Marks: "))
        self.__c = int(input("Enter Chem Marks: "))
        self.__m = int(input("Enter Maths Marks: "))

    def printBsc(self):
         self.printStudentInfo()
         print("Marks in different Subjects : ", self.__p,self.__c,self.__m)

    def calcTotalMarks (self):
        return(self.__p+self.__m+self.__c)

class Result(Bsc):
    def getResult(self):
        self.getBsc()
        self.__total=self.calcTotalMarks()

    def putResult(self):
        self.printBsc()
        print("Total Marks out of 300 : ", self.__total)

student = Result()
student.getResult()
student.putResult()