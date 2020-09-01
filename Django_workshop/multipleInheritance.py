class ClassA:
    a = 10
    def method_1():
        print("This is Parent Class 1")
        return

class ClassB:
    b=20
    def method_2():
        print("This is Parent Class 2")
        return

class ClassC(ClassA, ClassB):
    c=30
    def method_3():
        print("This is Child Class")
        return

ob = ClassC
print(ob.a, ob.b, ob.c)

ob.method_1()
ob.method_2()
ob.method_3()
