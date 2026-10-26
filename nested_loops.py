print("=====ATM=====")
total100=total50=total20=total10=total5=total1=0
serving=True
money_dispensed=0
costumer_served=0
while serving:
    name=input("what is your name : ")
    amount=int(input("how much money do you want to withdraw"))
    print("hello",name)
    if amount<=0:
        print("invalid amount")
        continue
    print(f"dispensing {amount} units for {name}")
    remaining=amount
    index=1
    while index<=6:
        if index==1:value=100
        elif index==2:value=50
        elif index==3:value=20
        elif index==4:value=10
        elif index==5:value=5
        else:value=1
        count=remaining//value
        if count>0:
            print(f"{count}*{value} unit notes {count*value}")
            remaining-=count*value
            if value==100:total100+=count
            elif value==50:total50+=count
            elif value==20:total20+=count
            elif value==10:total10+=count
            elif value==5:total5+=count
            else:total1+=count
    index+=1
    costomer_served+=1
    