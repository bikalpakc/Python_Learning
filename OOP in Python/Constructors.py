class Person:
    def __init__(self, f, l):
        self.fname=f
        self.lname=l

    def fun1(self):
        print(f"{self.fname}'s surname is {self.lname}")

obj1=Person("James", "Shrestha")
obj2=Person("Immanual", "Shah")

obj1.fun1()
obj2.fun1()   