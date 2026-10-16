mic=3
camera=6
storage=9
location=5
approved_apps=[
    "coding app"
    "chat app"
    "homework app"
    "school app"
    "Internet app"
]
name=input("enter your name")
request_app=input("enter the type of the app  you want approved :").strip().lower()
#i did app type because then it can actually check the app 
print("\n---identity operator---")
if type(name) is str:
    print("your name is stored as a string")
if type(request_app) is not int:
    print("the requested app is not stored as a number")
print("\n---membership operator---")
if request_app in approved_apps:
    print("this app is student approved")
else:
    print("this is not student approved")
restricted_apps=[
    "youtube"
    "social media apps"
    "gaming app"
    
]
if request_app not in restricted_apps:
    print("this app type is not in restrcted area")
else:
    print("this app typeis in the restricted area")
print("\n---app settings--")
student=mic| location | storage | camera
print("permission value :",student)
print("value in bits:",bin(student))
if student & mic:
    print("microphone access Enable")
if student & location:
    print("Location access enable")
else:
    print("Location access disabled")
if student & storage:
    print("storage access enable")
if student & camera:
    print("camera access enable")
print("\n---bit shift---")
next_permission=camera<<1
print("camera bit",bin(camera))
print("after right shift",bin(next_permission))
previos_permission=storage>>1
print("storage bit",bin (storage))
print("after left shift",bin(previos_permission))
print("\n---final access results---")
if request_app in approved_apps and request_app not in restricted_apps:
    print("access granted to",request_app,)
else:
    print("access granted to",request_app)