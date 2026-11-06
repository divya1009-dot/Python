def factorial(y):
    """this a recursive function to find the factorial"""
    if y==0 or y==1:
        return 1
    else:
        return y * factorial(y-1)
print(factorial.__doc__)
print("factorial of 36: ",factorial(36))
print("factorial of 29: ",factorial(29))
print("factorial of 5: ",factorial(5))
print("factorial of 47: ",factorial(47))