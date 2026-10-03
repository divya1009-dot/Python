name=input("enter your name")
club=input("Enter your club name")
points=9.5
member_number=8
Status=True
print("NAME:",name),type(str)
print("CLUB:",club),type(str)
print("POINTS:",points),type(float)
print("MEMBER NUMBER:",member_number),type(int)
print("ACTIVE:",Status),type(bool)
badge_code=(name[0:3]+club[-1]+member_number)
print("CODE:",badge_code)
print("\n=======Club Badge=======")
print("MEMBER:",name)
print("CLUB:",club)
print("CODE:",badge_code)
print("POINTS",points,"|""ACTIVE:",Status)