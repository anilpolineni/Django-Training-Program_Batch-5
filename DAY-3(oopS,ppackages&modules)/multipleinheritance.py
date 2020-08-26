class classA:
    x,y=10,20

    def method1():
        return ('i"m from classA')

class classB:
    a,b=50,60

    def method2():
        return ('i"m from classB')

class classC:
    p,q=100,200

    def method3():
        return ('i"m from classC')

class classD(classA,classB,classC):
    s,t=1,2

    def method4():
        return ('i"m from classD')

obj=classD
print(obj.p,obj.q,obj.method3())
