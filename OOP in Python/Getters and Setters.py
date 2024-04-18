

class Demo():
    def __init__(self, value) -> None:
        self.value1= value

    @property
    def value(self):
        return self.value1    

    @value.setter
    def new_value(self, value):
        self.value1=value

obj1=Demo(10)
obj1=20
print(obj1.value1)        
