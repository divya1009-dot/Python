def greet_customer():
    print("Welcome to the Art Supplies Store!")
    print("Get your art supplies.")
greet_customer()
price_per_item = float(input("Enter the price per item in dollars: "))
items_bought = int(input("Enter the number of items bought: "))
def cal_total(price, items):
    total = price * items
    return total
total_cost = cal_total(price_per_item, items_bought)
rounded_total = round(total_cost, 2)
print("Total Cost:", rounded_total)
payings = float(input("Enter the amount paid by you: "))
def change(paid, total):
    change = paid - total
    return change
change_due = change(payings, rounded_total)
rounded_change = round(change_due, 2)
def thank_you_message(items):
    if items >= 5:
        return "thank you! for picking many art supplies"
    else:
        return "Thanks for shopping at my store!"
closing_message = thank_you_message(items_bought)
print("")
print("===== ART SUPPLIES BILL =====")
print("Price Per Item:", price_per_item)
print("Items Bought:", items_bought)
print("Total Cost:", rounded_total)
print("Amount Paid:", payings)
print("Change Due:", rounded_change)
print(closing_message)
print("=============================")
