a=int(input("enter a value"))
b= int(input("enter a value 2"))
c=int(input("enter a value 3"))
avg=(a+b+c)/3
if avg>a and avg > b and avg> c:
    print("avg is greater than a b c ")
elif avg>a:
    print("avg greater than a")
elif avg>a and avg>b:
    print ("avg is greater than a and b") 
elif avg>a and avg > c:
    print("avg is greater than a and c")
elif avg>c and avg>b:
    print("avg is greater than b and c")
elif avg>b:
    print ("ang is greater than b")
elif avg>c:
    print ("avg is greater than ")