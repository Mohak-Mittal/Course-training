def b(a):
    def c():
        print("============")
        a()
        print("============")
    return c

@ b
def a():
    print("hello world")

a()