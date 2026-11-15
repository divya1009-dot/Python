valid=False
while not valid:
    try:
        bill=float(input('what is the bill? '))
        dis=float(input('how much discount? '))
        people=int(input("how many people are there"))
        discount_amount=bill*dis/100
        total_bill=bill-discount_amount
        per_person=total_bill/people
    except ValueError as i:
        print("Exception : ",i)
    except ZeroDivisionError:
        print('you cannot divide people by 0')
    else:
        print("Final Bill : ",total_bill)
        print("price per person : ",per_person)
        valid=True
    finally:
        print("Attempt finished")