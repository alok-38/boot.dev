x = 5
def f():
    y = 10
    print(x)

def g():
    z = 20
    def h():
        a = 1
        print(a, z)

f()
g()

