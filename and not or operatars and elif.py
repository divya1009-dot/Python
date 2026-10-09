day=(input("enter the day monday/sunday")).strip().capitalize()
homework=(input("have you finished your homework yes/no")).strip().lower()
weather=(input("what's the weather sunny/cloudy/rainy")).strip().lower()
print("your plan for ",day)
if day in ("Saturday","Sunday"):
    print("Day type:weekend")
elif day=="Monday":
    print("Day type: first day of the week")
elif day=="Friday":
    print("Day type: last school day")
elif day in ("Tuesday","Wednesday","Thursday"):
     print("Day type: regular school day")
else:
    print("day not recognised")
if weather=="sunny" and homework=="yes":
    print("after school head to the park")
if weather=="rainy" or weather=="cloudy":
    print("pack your umbrella")
if homework != "yes":
    print("finish it before going out")
if weather=="rainy" and not homework==("yes"):
    print("Best plan: finish your homework then watch your favourite TV show")
elif weather=="sunny" and homework=="yes" and not (day in ("Saturday","Sunday")):
    print (" all set for a good school day")
else:
    print("best plan: take it one step at a time")