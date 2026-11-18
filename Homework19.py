print("I am a function calculator")
cal=input(" what do you want to do add, subtract, multiply, divide")
def multiply():
    try:
        a=float(input("what do you want to multiply"))
        b=float(input("by how much?"))
        result=a*b
        return result
    except ValueError as t:
        print(t)
    finally:
        print("thank you for using me")
def add():
    try:
        a=float(input("what do you want to add to"))
        b=float(input("by how much?"))
        result=a-b
        return result
    except ValueError as t:
        print(t)
    finally:
        print("thank you for using me")
def divide():
    try:
        a=float(input("what do you want to divide "))
        b=float(input("by how much?"))
        result=a/b
        return result
    except ValueError as t:
        print(t)
    except ZeroDivisionError as r:
        print(r)
    finally:
        print("thank you for using me")
def subtract():
    try:
        a=float(input("what do you want to subract from"))
        b=float(input("by how much?"))
        result=a-b
        return result
    except ValueError as t:
        print(t)
    finally:
        print("thank you for using me")
if cal=="add":
    to=add()
    print(f" the answer is {to}")
elif cal=="subtract":
    to=subtract()
    print("the answer is",to)
elif cal=="multiply":
    to=multiply()
    print("the answer is",to)
elif cal=="divide":
    to=divide()
    print("the answer is",to)
else:
    print('invalid input, copy it letter for letter as written')