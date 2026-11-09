def total_bill(bill, tip):
    total=bill*(1+0.1*tip)
    total=round(total, 2)
    print(f"pay ${total}")
total_bill(150, 20)
def seating_arangement(guest):
    """this is a recursive case that does the seating arangment"""
    if guest==1 or guest==0:
        return 1
    else:
        return guest*seating_arangement(guest-1)
print(seating_arangement.__doc__)
print("seating arrangements for 20 guests",seating_arangement(20))
print("seating arrangements for 48 guests",seating_arangement(48))
print("seating arrangements for 5 guests",seating_arangement(5))
print("seating arrangements for 2 guests",seating_arangement(2))
print("seating arrangements for 5 guests",seating_arangement(5))