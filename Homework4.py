print("=====Swimming pool entry checker=====")
can_swim=(input("Can you swim 25 meters yes/no")).lower().strip()
age=int(input("how old are you")).strip()
adult= (input("is there an adult with you yes/no")).lower().strip()
print("\n=====Entry Desicion=====")
if age < 4:
    print("you are a toddler")
    print("go in the splash pool accompnied by an adult")
elif age < 12:
    print("you are a child")
    print("you can go to the main pool accompnied by an adult")
elif age < 18:
    print("you are a teenager")
    print("you can go to the main pool if you can swim")
else:
    print("you are an adult")
    print("all pools are open to you")
if can_swim != "yes" and can_swim != "no":
    print("input error enter a normal answer")
    swim_known=False
else:
    swim_known=True
if adult != "yes" and adult != "no":
    print("input error enter a normal answer")
    adult_known=False
else:
    adult_known=True
if adult=="yes" and can_swim=="yes":
    print("you can go to the deep end")
if age<12 or can_swim=="no":
    print("WARNING! stay in the shallow end today")
if adult_known==True and adult!="yes":
    print("Adult not there Remind the lifeguard to be alert")
if swim_known=="False" or adult_known=="True":
    print("Verdict: cannot decide untill both Questions asked answered properly")
elif age>=18 and can_swim=="yes":
    print("Verdict :Enjoy your swim you have full access")
elif age>=12 and can_swim=="yes" and adult=="yes":
    print("Verdict :Enjoy your swim you can go in the main pool withyour adult close to you")
elif can_swim=="no" and not adult=="yes":
    print(" Verdict :you can swim in the shallow end ,after you have an adult with you")
else:
    print ("Verdict :only shallow end today with an adult you can access more ")