# parameterised constructor
class student:

    def __init__(self,name):
        print('this is parameterised constructor')

        self.name=name # self.name global variable

    def show(self):
        return('hello',self.name)
stu=student('sairam')
print(stu.show())

        
        
