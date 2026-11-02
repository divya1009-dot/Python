def greet_customer():
    print("Hello customer welcome!")
    print("This is my lemonade stand!")
greet_customer()
price_per_cups=float(input("Enter the price in dollars : "))
cups_sold=int(input("how many cups are you buying? "))
def calculating(cup, price):
    total=price*cup
    return total
total_cost=calculating(price_per_cups, cups_sold)
rounded_total=round(total_cost, 2)
print("Total cost : ",rounded_total)
payings=float(input("how much money did you pay"))
def change_calculate(amount, userpay):
    change=userpay-amount
    return change
changes=round(change_calculate(rounded_total, payings),2)
def thanks(cups):
    if cups>=5:
        return"Wow a big order! thank you so much for you support"
    else:
        return"thank you for stopping by!"
closing_message=thanks(cups_sold)
print("\n\n=====Lemonade stand recipt=====")
print("price per cup : ",price_per_cups)
print("cups sold     : ",cups_sold)
print("toal amount   :",rounded_total)
print("Change due    :",changes)
print(closing_message)
print("================================")