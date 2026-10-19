mark1=int(input("enter marks"))
mark2=int(input("enter marks"))
mark3=int (input("enter marks"))
mark4=int(input("enter marks"))
mark5=int(input("enter marks"))
total=mark1+mark2+mark3+mark4+mark5
average=int(total/5)
validity=range(1,101)
if average not in validity:
    print("invalid input")
elif average in range (81,101):
    print("your grade is A")
elif average in range(61,81):
    print("your grade is B") 
elif average in range (61,41):
    print("your grade is C")
elif average in range (41,21):
    print("your grade is D")
else:
    print("your grade is F")