pending_chores=4
original_count=pending_chores
print("you have ",original_count," chores to finish")
completed_chores=0
chore_number=1
while chore_number<=pending_chores:
    chore_number+=1
    if chore_number==1:chore="make your bed" 
    elif chore_number==2:chore="feed the pet"
    elif chore_number==3:chore="take out the trash"
    else: chore="wash the dishes"
    answer=input(f"have you comleted{chore} yes/no")
    if answer=="yes":
        completed_chores+=1
        chore_number+=1
        print("great job! chore completed")
    else:
        print("go back and finish it")
    print("chores remaining:",pending_chores-completed_chores)
print("======you have completed your chores======")
print("now let's take a look at the infinity loop")
safety_counter=0
test_value=0
while test_value<=0:
    print('hello')
    safety_counter+=1
    if safety_counter>=3:
        print("stopping here on purpose...infinity loops never stop")
        break
print("=======SUMMARY=======")
print("chores assigned today: ",pending_chores)
print("chores completed: ",completed_chores)
print("chores remaining: ",pending_chores-completed_chores)