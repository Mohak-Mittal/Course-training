# from abc import ABC,abstractmethod

# class boss(ABC):
#     @abstractmethod
#     def abc(self):
#         print ("hi employee good morning")
# class employee1(boss):
#     def abc(self):
#         super().abc()
#         print("hi boss good morning ep 1 here")
# class employee2(employee1):
#     def abc(self):
#         super().abc()
#         print("hi boss good morning ep 2 here")
# e1 = employee2()
# e1.abc()

class abc:
    def __init__ (self,a):
        self.__a = a
    def show(self):
        return self.__a
a = abc(5000)
print(a.show())
a.__a = -1000
print(a.show())