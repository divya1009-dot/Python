try:
    num1=int(input('enter a first number '))
    num2=int(input('Enter a second number'))
    result=num1/num2
    print("the result is ",result)
except ZeroDivisionError as t:
    print("Exception : ",t)
except ValueError as r:
    print("Exception : ",r)
except:
    print("Wrong input")
else:
    print("no exceptions")
finally:
    print("this will excecute no matter what")