field_1=150
field_2=80
field_3=170
field_4=60
field_5=100
total=field_1+field_2+field_3+field_4+field_5
average=total/5
print("total harvest :",total)
print("average per field :",average)
price_per_kg=20
total_earnings=total*price_per_kg
print("Total Earnings .Rs :",total_earnings)
bags=total//25
leftovers=total%25
print("full bags packed:",bags)
print("left over bag kg:",leftovers)
last_year=530
print("better then last year",total>last_year)
print("same as last year",total==last_year)
print("worse than last year",total<last_year)
total+=50
print("after bonus crop",total)
total-=20
print ("after seed reserve",total)
bags_changed=total//30
print ("total bags packed",bags_changed)
