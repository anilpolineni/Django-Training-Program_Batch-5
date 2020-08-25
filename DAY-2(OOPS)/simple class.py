'''class sample:
    name='Python'

    def hi():
        return('welcome to apssdc')

print(sample.name)
print(sample.hi())'''

'''
# arthematic operations

class hello:
    print('Arthrmatic opertaions')

    def add():
        a=100
        b=200
        return('addition of %d + %d is %d'%(a,b,a+b))

print(hello.add())'''

# Dymamic values

class operations:
    print('Arthrmatic opertaions')

    def  addition(a,b):
        return ('addition of %d +%d is %d'%(a,b,a+b))
    def sub(a,b):
        return ('addition of %d - %d is %d'%(a,b,a-b))

a=int(input('enter a value'))
b=int(input('enter b value'))

print(operations.addition(a,b))
print(operations.sub(a,b))

                



