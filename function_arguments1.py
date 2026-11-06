def cal_total(bill_amount, tip_perc):
    total=bill_amount*(1+0.01*tip_perc)
    total=round(total,2)
    print(f"total bill is ${total}")
cal_total(150, 20)