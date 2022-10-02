#1
print("1.")
class Rectangle:
    def __init__ (self,color = "green", width = 100, height = 100, justchange = 0):
        self.color = color
        self.width = width
        self.height = height
        self.justchange = justchange
    def square(self):
        return self.width * self.height
    def setjustchange(self, number):
        self.justchange = number
        print(self.justchange)
rect1 = Rectangle()
print(rect1.color)
print(rect1.square())
rect1 = Rectangle("yellow", 23, 34)
print(rect1.color)
print(rect1.square())
print("\n")
print(rect1.justchange)
rect1.setjustchange(7)
print("\n")



#2
print("2.")
class Person:
    def __init__(self,f_name,l_name):
        self.f_name = f_name[0].upper() + f_name[1:len(f_name)].lower()
        self.l_name = l_name[0].upper() + l_name[1:len(l_name)].lower()
    def __repr__(self):
        print(f'{self.f_name} {self.l_name}')
person1 = Person("JOHN", "sMiTh")
print(person1.f_name)
print(person1.l_name)
person1.__repr__()
print("\n")



#3
print("3.")
class Calculator:
    def add(self):
        print(a + b)
    def sub(self):
        print(a - b)
    def mult(self):
        print(a * b)
    def div(self):
        print(a / b)
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
obj = Calculator()
choice = 1
while choice != 0:
    print("Enter 1 to add")
    print("Enter 2 to subtract")
    print("Enter 3 to multiply")
    print("Enter 4 to divide")
    print("Enter 0 to exit")
    choice = int(input("Choose one: "))
    if choice == 1:
        print(obj.add())
    elif choice == 2:
        print(obj.sub())
    elif choice == 3:
        print(obj.mult())
    elif choice == 4:
        print(obj.div())
    elif choice == 0:
        print("Bye)")
    else:
        print("Error")
