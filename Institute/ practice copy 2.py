# # # # # # # # # # class department:
# # # # # # # # # #     pass
# # # # # # # # # #     def bca(self):
# # # # # # # # # #         print("BCA Department")
# # # # # # # # # #     def bba(self):
# # # # # # # # # #         print("BBA Department")
# # # # # # # # # #     def mca(self):
# # # # # # # # # #         print("MCA Department")
# # # # # # # # # #     def mba(self):
# # # # # # # # # #         print("MBA Department")
# # # # # # # # # # D = department()
# # # # # # # # # # D.bca()
# # # # # # # # # # D.mba()
# # # # # # # # # # D.bba()

# # # # # # # # # class teacher:
# # # # # # # # #     pass

# # # # # # # # # a = teacher()
# # # # # # # # # mca = teacher()
# # # # # # # # # mca.id = 102
# # # # # # # # # mca.name = "Mohit"
# # # # # # # # # mca.age = 25
# # # # # # # # # bca = teacher()
# # # # # # # # # bca.id = 103
# # # # # # # # # bca.name = "Mohak"
# # # # # # # # # bca.age = 22

# # # # # # # # # print(mca.id,mca.name,mca.age)
# # # # # # # # # print(bca.id,bca.name,bca.age)

# # # # # # # # class atm:
# # # # # # # #     def withdraw(self,balance,amount):
# # # # # # # #         if amount <= balance:
# # # # # # # #             balance -= amount
# # # # # # # #             print("Withdraw")
# # # # # # # #             return balance
# # # # # # # #         else:
# # # # # # # #             print("Insufficient Balance")
# # # # # # # #     def diposite(self,balance,amount):
# # # # # # # #         balance += amount
# # # # # # # #         print("Diposite")
# # # # # # # #         return balance
# # # # # # # #     def checkbalance(self,balance):
# # # # # # # #         print("Check Balance")
# # # # # # # #         return balance
# # # # # # # # A = atm()
# # # # # # # # balance = 10000
# # # # # # # # amount = int(input("enter the amount : "))
# # # # # # # # print("what do you want to do\n 1 for withdraw\n 2 for diposite\n 3 for checkbalance")
# # # # # # # # op = int(input("enter your option : "))
# # # # # # # # if op == 1:
# # # # # # # #    print(A.withdraw(balance,amount))
# # # # # # # # elif op == 2:
# # # # # # # #     print(A.diposite(balance,amount))
# # # # # # # # elif op == 3:
# # # # # # # #     print(A.checkbalance(balance))
# # # # # # # # else:
# # # # # # # #     print("Invalid option")

# # # # # # # class person:
# # # # # # #     def home(self):
# # # # # # #         print("Home")
# # # # # # # class child(person):
# # # # # # #     def toys(self):
# # # # # # #         print("Toys")
        
# # # # # # # c = child()
# # # # # # # c.home()
# # # # # # # c.toys()
    
# # # # # # class teacher:
# # # # # #     def teach(self):
# # # # # #         print("Teaching")
# # # # # # class student1(teacher):
# # # # # #     def study(self):
# # # # # #         print("Studying in class 1")
# # # # # # class student2(teacher):
# # # # # #     def study(self):
# # # # # #         print("Studying in class 2")
# # # # # # class student3(teacher):
# # # # # #     def study(self):
# # # # # #         print("Studying in class 3")
        
# # # # # # a = student1()
# # # # # # a.teach()
# # # # # # a.study()

# # # # # # b = student2()
# # # # # # b.teach()
# # # # # # b.study()

# # # # # # c = student3()
# # # # # # c.teach()
# # # # # # c.study()

# # # # # # class grandfather:
# # # # # #     def grand(self):
# # # # # #         print("I am grandfather")
# # # # # # class father(grandfather):
# # # # # #     def fath(self):
# # # # # #         print("I am father")
# # # # # # class son(father):
# # # # # #     pass
# # # # # # c = son()
# # # # # # c.grand()
# # # # # # c.fath()

# # # # # class grandfather:
# # # # #     def grand(self):
# # # # #         print("I am grandfather")
# # # # # class father (grandfather):
# # # # #     def fath(self):
# # # # #         print("I am father")
# # # # # class uncle(grandfather):
# # # # #     def uncle(self):
# # # # #         print("I am uncle")
# # # # # class son(father):
# # # # #     pass
# # # # # class daughter(uncle):
# # # # #     pass

# # # # # s =son()
# # # # # d = daughter()
# # # # # s.grand()
# # # # # s.fath()
# # # # # d.grand()
# # # # # d.uncle()

# # # # class father:
# # # #     def fat(self):
# # # #         print("hello i am father")
# # # # class mother:
# # # #     def mot(self):
# # # #         print("hello i am mother")
# # # # class child(father,mother):
# # # #     pass
        
# # # # c =child()
# # # # c.mot()
# # # # c.fat()

# # # class teach:
# # #     def t(self):
# # #         print("i am a teacher")
# # # class student1(teach):
# # #     def s1(self):
# # #         print("i am student1")
# # # class student2(teach):
# # #     def s2(self):
# # #         print("i am student2")
# # # class student3(student1,student2):
# # #     pass

# # # s = student3()
# # # s.s1()
# # # s.s2()

# # it is a process of hiding impimation details and show only necessary features
# from abc import ABC,abstractmethod
# class abc (ABC):
#     @abstractmethod
#     def ABC(self):
#         print("hi")
# class pqr (abc):
#     def ABC(self):
#         super().ABC()
#         print("hello i am pqr")
# p = pqr()
# p.ABC()


class school:
    school = "SVM SCHOOL"
    @classmethod
    def student(cls):
        cls.name = input("enter the name : ")
        cls.age = int(input("enter age : "))
        cls.grade = int(input("enter grade : "))
        print(cls.name,cls.age,cls.grade,cls.school)
    def teacher(self):
        self.name = input("teacher name : ")
        self.age = int(input("teacher age : "))
        self.subject = input("teacher subject : ")
        print(self.name,self.age,self.subject,school.school)
    @staticmethod
    def schooltime():
        print("time is 10:00AM")
school.student()
s = school()
s.teacher()
s.schooltime()