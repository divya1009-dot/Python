mark1=int(input("enter marks"))
mark2=int(input("enter marks"))
mark3=int (input("enter marks"))
mark4=int(input("enter marks"))
total=mark1+mark2+mark3+mark4
average=int(total/4)
validity=range(1,101)
if average not in validity:
    print("invalid input")
elif average in range (81,101):
    print("your grade is a one")
elif average in range(61,81):
    print("your grade is b1") 