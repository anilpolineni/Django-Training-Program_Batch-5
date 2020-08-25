class math:
    def __init__(abc,x,y):
        abc.p=x
        abc.q=y

    def add(abc):
        return ('addition of two numbers is',abc.p+abc.q)
    def sub(abc):
        return ('subctraction of two numbers is',abc.p-abc.q)

x=int(input('enter x value'))
y=int(input('enter y value'))


obj=math(x,y)

print(obj.add())
print(obj.sub())
        
