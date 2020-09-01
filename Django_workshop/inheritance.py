class ClassA:
    a, b = 10, 20

    def method_1():
        return ("I'm from Class A")

class ClassB(ClassA):

    c, d = 30, 40

    def method_2():
        return("I'm from Class B")

obj = ClassB
print(obj.a)
print(obj.method_1())
print(obj.c)
print(obj.method_2())
