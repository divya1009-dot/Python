print("====================")
print(" My Holiday planner")
print("====================\n")
print("step 1-pick your holiday")
print("beach holiday=1")
print("mountain holiday=2")
choice=int(input("which holiday do you choose"))
if choice==1:
    print("you picked beach holiday")
    print("Step 2-pick your activity")
    print("swimming=1")
    print("sandcastle building=2")
    act_choice=int(input("which activity do you choose"))
    if act_choice==1:
        print("you choose Swimming")
        print("best time: Morning")
        print("reminder: Take sunscream and water with you")
    elif act_choice==2:
        print("you choose Sandcastle Building")
        print("best time: Evening")
        print("reminder: Take a shovel and a bucket")
    else:
        print("invalid input")
        print("enter 1 or 2")
elif choice==2:
    print("you choose a Mountain Holiday")
    print("camping=1")
    print("hiking=2")
    act_choice=int(input("which activity do you choose"))
    if act_choice==1:
        print("you choose camping")
        print("best for: staying close to nature")
        print("remember: take a tent and a flashlight")
    elif act_choice==2:
        print("you choose hiking")
        print("best for: Exploring trails")
        print("remember: wear comfortable shoes")
    else:
        print("invalid choice")
        print("enter 1 or 2")
else:       
    print("invalid choice ")
    print("enter 1 for beach holiday or 2 for mountain holiday")
print("\n==================================")
print("  YOUR HOLIDAY PLAN IS COMPLETE")
print("        ENJOY THE TRIP")
print("==================================")