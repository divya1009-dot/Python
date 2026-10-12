x=7
if (type(x) is int):
    print("True")
else:
    print("False")
x=7.2
if (type(x)is not float):
    print("True")
else:
    print("False")
x=30
y=30
if (x is y):
    print("x and y are the same identity")
y=25
if (x is not y):
    print("x is not y")