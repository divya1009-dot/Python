def cal_change(paid, price):
    change=paid-price
    return change
snack_price=25
print("=====snack machine=====")
print(f"you have to pay ${snack_price}")
print("accepted coins : 1, 5, 10, 20, 25")
total_inserted=0
coins_inserted=0
while True:
    coins=int(input("insert a coin 1, 5, 10, 20, 25 and write it here : "))
    if coins!=1 and coins!=5 and coins!=10 and coins!=20 and coins!=25:
        print("invalid coins")
        continue
    total_inserted+=coins
    coins_inserted+=1
    print(f"coins inserted {coins_inserted}. total so far ${total_inserted}")
    if snack_price<=total_inserted:
        print("enjoy your snack\n")
        break
change_due=cal_change(total_inserted, snack_price)
print("dispensing a snack...")
if change_due==0:
    pass
else:
    print(f"here's your change : {change_due} units")
print("=====Purchase Summary=====")
print("snack price    : ",snack_price)
print("coins inserted : ",coins_inserted )
print("total paid     : ", total_inserted)
print("change given   : ",change_due )
print("Thanks for a purchase!")