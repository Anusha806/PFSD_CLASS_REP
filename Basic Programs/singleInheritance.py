class parent:
    def function1(self):
        print("This is my 1st Function ")

class child(parent):
    def function2(self,a):
        print("This is my 2nd function ")
        print(a)
    b=10

y=child()
y.function1()
y.function2(5)
print(y.b)