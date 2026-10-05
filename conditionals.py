temperature=int(input("entertodays temperature in celcius"))
if(temperature<20):
    outfit="jacket"
    print ("it is cold today wear a ",outfit)
else:
    outfit="T-shirt"
    print ("it is warm today wear a ",outfit)
is_raining=(input("is it raining today"))
if is_raining=="yes":
    print("bring an umbrela")
wind_speed=int(input("enter the wind speed"))
if wind_speed>30:
    windbreaker="yes"
    print("it is windy today")
    print("wear a windbreaker over your",outfit)
else:
    windbreaker="no"
    print("it is calm today")
    print("no windbreaker needed over your ",outfit)
has_puddles=input("are there puddles on the ground")
if has_puddles=="yes":
    shoes="boots"
    print ("the ground is wet,wear",shoes)
else:
    shoes="sneakers"
    print ("the ground is dry,wear",shoes)
print("weather check complete")
print("\n =======WEATHER OUTFIT PICKER=======")
print("Temperature:",temperature)
print("Outfit Chosen:",outfit)
print("is it Raining?",is_raining)
print("wind breaker needed?",windbreaker)
print("Shoes chosen",shoes)
print("======================================")

