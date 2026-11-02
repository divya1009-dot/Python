print("===Star pyramid pattern===")
rows=int(input("enter the number of rows : "))
for i in range (rows):
    for j in range (i+1):
        print("*",end="")
    print()
print("===Floyids triangle===")
number=1
row=int(input("how many rows should it have?: "))
for i in range (1,row+1):
    for j in range (1,i+1):
        print(number,end=" ")
        number+=1
    print()
rows_num=int(input("Enter the number of rows : "))

if rows_num%2==0:
    halfdiomond=int(rows_num/2)
else:
    halfdiomond=int(rows_num/2+1)
space=halfdiomond-1
for i in range (1,halfdiomond+1):
    for j in range (1,space+1):
        print(end=" ")
    space-=1
    num=1
    for k in range (2*i-1):
        print(num,end="")
        num+=1
    print()
space=1
for i in range (1,halfdiomond):
    for j in range (1,space+1):
        print(end=" ")
    space+=1
    num=1
    for k in range (1,2*(halfdiomond-i)):
        print(num,end="")
        num+=1
    print()
print("\n==============================Loop disign complete!=============================")
print("you have made a pyramid,Floyeds pyramid and a diomong using nested loops")
print("="*80)