def cal_change(price, paid):
    change=price-paid
    return change
ticket_cost=30
print("=====Parking Ticket Helper=====")
print(f"your parking ticket costs ${30}")
print("accepted coins are : 1, 5, 10, 20, 25")
coins_inserted=0
total_paid=0
while True:
    coin=int(input("which coin did you enter "))
    if coin !=1 and coin !=5 and coin !=10 and coin !=20 and coin!=25:
        print("invalid coin")
        continue
    total_paid+=coin
    coins_inserted+=1
    print(f"coins inserted {coins_inserted}. Total so far {total_paid}")
    if total_paid>=ticket_cost:
        print("Enough money inserted")
        break
change_due=cal_change(total_paid, ticket_cost)
print ("dispensing ticket...")
if change_due==0:
    pass
else:
    print(f"here's your change {change_due} units")
print("\n\n=====Parking Ticket Summary=====")
print("Ticket Price   : ",ticket_cost)
print("Price Paid     : ",total_paid)
print("Coins Inserted : ",coins_inserted)
print("Change given   : ",change_due )