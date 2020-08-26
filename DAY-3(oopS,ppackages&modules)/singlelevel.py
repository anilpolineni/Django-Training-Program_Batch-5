class classA:
    a,b=10,20

    def method1():
        return ('i"m from ClassA')


class classB(classA):
    c,d=30,40

    def method2():
        return ('i"m from classB')

obj=classB
print(obj.d)
print(obj.method2())
