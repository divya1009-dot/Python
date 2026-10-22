print("=====MY Power Calculator=====")
num=int(input("enter a number"))
power_num=int(input("to the power of?"))
result=1
for i in range (1,power_num +1):
    result=result*num
    print("step:",i," result: ",result)
print("\nAnswer: ",num,"to the power of",power_num,"=",result)