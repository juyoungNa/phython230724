class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
    def working(self):
        print("현재 작업중")
    def coding(self):
        print("현재 코딩중")

class Student(Person):
    #상속받고 덮어쓰기(재정의, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 부모클래스 초기호 메서드 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
        print("Info(Subject:{0}, StudentID: {1})".format(self.subject, self.studentID))

#인스턴스
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "AI금융공학", "201234")
p.printInfo()
s.printInfo()
s.coding()
s.working()

print(s.__dict__)