print("===Grocery Billing Queue")
low_price_items=medium_price_items=high_price_items=0
customers_served=0
total_sales=0
billing=True
while billing:
    name=input("what is your name?  ")
    items=int(input("how many items are you buying?  "))
    if items<=0:
        print("Error enter a positive number")
        continue
    customer_total=0
    item_num=1
    while item_num<=items:
        item_name=input("what is your items name ")
        quantity=int(input("how much quantity is it "))
        price=int(input("how much does it cost "))
        if price<=0 or quantity<=0:
            print("Error prce or quantity is not a positive number check again")
        item_total=quantity*price
        print(f"{item_name}: {quantity}*{price}={item_total}")
        customer_total+=item_total
        if item_total<=50:
            low_price_items+=quantity
        elif item_total<=100:
            medium_price_items+=quantity
        else:
            high_price_items+=quantity
        item_num+=1
    customers_served+=1
    total_sales+=customer_total
    print(f"\n Total bill for {name} is {customer_total}.billing Complete!\n\n")
    again=input("next costumer? yes|no").lower().strip()
    if again!="yes":
        billing=False
print("\n=== Grocery Category Report ===")
for slot in range(1, 4):
    if slot == 1:
        label, total = "Low price items", low_price_items
    elif slot == 2:
        label, total = "Medium price items", medium_price_items
    else:
        label, total = "High price items", high_price_items
    if total > 0:
        print(f"  {label}: {total} ", end="")
        for item in range(total):           
            print("*", end="")
        print()
print(f"\nCustomers served : {customers_served}")
print(f"Total sales      : {total_sales}")
print("Grocery billing closed. Goodbye!")