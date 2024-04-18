class Employee_Details:
    def __init__(self, name, department):
        self.name=name
        self.department=department

    def display(self):
        print(self.name, self.department)    

class Additional_Details(Employee_Details):
    def __init__(self, name, department, salary):
        super().__init__(name, department)
        self.salary=salary

    def display_details(self):
        print(self.name, self.department, self.salary)

employee1=Employee_Details("Ramsey", "A Doggy")
employee1.display()
employee2=Additional_Details("Joshua", "Labour", "Rs.500 per day")
employee2.display_details()