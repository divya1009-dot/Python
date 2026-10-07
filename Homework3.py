homework=int(input("enter your homework time in minutes"))
if homework>60:
   print("that is a long session")
   print("get to work now")
else:
   print("finish it quickly")
   print("it is a short session")
freetime=(input("do you have freetime yes/no"))
if freetime=="yes":
   print("find a hobby to fill un the time")
print("\n=====Daily Plan=====")
print("homework time:",homework)
print("freetime:",freetime)
if freetime=="yes":
   print("find a hobby to fill in that time")
   print("sugguestions:a fight sport,music instrument or football or badminton or tennis")
print("====================")