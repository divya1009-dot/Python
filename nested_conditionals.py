print("====================")
print("your vechicle picker")
print("====================")
print()
print("1=car")
print("2=bike")
choice=int(input("which vechicle do you choose"))
if choice==1:
    print("you chose a car pick your car type")
    print("1=Sedan")
    print("2=SUV")
    car_choice=int(input("which type do you choose"))
    if car_choice==1:
        print("you choose a Sedan")
        print("it is a 5 seater")
        print("best for family trips")
    else:
        print("you choose SUV")
        print("it is a 7 seater")
        print("best for off-road adventures")
elif choice==2:
    print("you picked a bike pick your bike type")
    print("1=scooty")
    print("2=mountain bike")
    bike_choice=int(input("which type do you choose"))
    if bike_choice==1:
        print("you picked scooty")
        print("top speed 80 km/h")
        print("best for city roads")
    else:
        print("you picked mountain bike")
        print("top speed 40 km/h")
        print("best for off road trails")
else:
    print("that was not a valid choice")
    print("enter 1 for car and 2 for bike")
print("YOUR CUSTOM RIDE IS READY ENJOY THE JOURNEY!")  