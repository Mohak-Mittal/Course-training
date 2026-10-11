from abc import ABC,abstractmethod

class Character:
    @abstractmethod
    def __init__(self,name):
        self.__name = name
        print(self.__name,"is ready for battle")
    def attack():
        pass
    def magic():
        pass

class Warrior(Character):
    def __init__(self,name,health,mana):
        super().__init__(name)
        self.__health = health
        self.__mana = mana
    def attack(self):
        print("Attack = ",self.__health)
    def magic(self):
        print("Magic = ",self.__mana)

class Mage(Character):
    def __init__(self,name,health,mana):
        super().__init__(name)
        self.__health = health
        self.__mana = mana
    def attack(self):
        print("Attack = ",self.__health)
    def magic(self):
        print("Magic = ",self.__mana)

class Hunter(Character):
    def __init__(self,name,health,mana):
        super().__init__(name)
        self.__health = health
        self.__mana = mana
    def attack(self):
        print("Attack = ",self.__health)
    def magic(self):
        print("Magic = ",self.__mana)

a = input("Enter your name: ")
print ("choose character avatar 1 for warrior and 2 for mage 3 for hunter")
b = int(input("Enter your choice: "))
if b == 1:
    w = Warrior(a,100,50)
    w.attack()
    w.magic()

elif b == 2:
    m = Mage(a,50,500)
    m.attack()
    m.magic()
    
elif b == 3:
    h = Hunter(a,80,50)
    h.attack()
    h.magic()
    

        