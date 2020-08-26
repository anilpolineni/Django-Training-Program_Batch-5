class classA:
    y,z=1000,2000

    def method1():
        return 'i",m from classA'

class classB(classA):
    e,f='hello','how r u'

    def method2():
        return 'i"m from classB'

class classc(classB):
    p,q='python','C-lang'
    
    def method3():
        return 'i"m from classC'

obj=classc()
print(obj.y,obj.z,obj.method1())
