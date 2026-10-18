riceprice=10
milkprice=9
baskets=12
fruitprice=6
family_members=4
basket_cost_per_person=(riceprice + milkprice + fruitprice)*baskets/family_members
print("basket cost per person:",basket_cost_per_person)
recorded_average=83
correction=59
wrong=46
total_weeks=3
rec_total=recorded_average*total_weeks
correct_total=rec_total-wrong+correction
corrected_average=correct_total/total_weeks
total_items=int(input("what are the total items"))
people=int(input("how many people are there"))
if people==0:
    print("you cannot share between 0 people")
if total_items%2==0:
    print("you can divide it equally")
    print("each person gets",total_items//family_members)
else:
    print("you cannot divide it equally")
storea=73
storeb=79
storec=80
average=(storea+storeb+storec)/3
if corrected_average>storea and corrected_average>storeb and corrected_average>storec:
    verdict=("store more expensive than all 3 stores") 
if corrected_average<storea and corrected_average<storeb and corrected_average<storec:
    verdict=("store cheaper than all 3 stores") 
else:
    verdict=("store is in between the 3 stores")

print("\n-----SUMMARY-----")
print("average cost per person:",basket_cost_per_person)
print("corrected weekly average:",corrected_average)
print("Verdict:",verdict)