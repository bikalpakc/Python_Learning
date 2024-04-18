class Person:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @classmethod
    def seperate_data(cls, unseperated_data):
        name, salary = unseperated_data.split("-")  
        return cls(name,salary)

unseperated_data="Simon-50000"
obj1=Person.seperate_data(unseperated_data)
print(f"The salary of {obj1.name} is {obj1.salary}")