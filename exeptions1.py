try:
    num=int(input('enter a number'))
    print("you entered the number",num)
except ValueError as ex:
    print("Exceptions: ",ex)