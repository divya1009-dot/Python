print("=====HOMEWORK COMPLETION TRACKER=====")
total_homework=4
original_count=total_homework
completed_count=0
task_num=1
while task_num<=total_homework:
    if task_num==1:
        next_task="maths worksheet"
    elif task_num==2:
        next_task="English writing"
    elif task_num==3:
        next_task="science reading"
    else:
        next_task="coding practice"
    answer=input(f"have you finished {next_task} yes/no").strip().lower()
    if answer=="yes":
        completed_count+=1
        task_num+=1
        print("great job! you have finished a homework task")
    else:
        print("finish it and check again")
    print("Homework tasks remaining:",total_homework-completed_count)
print("===Homework Complete===")
print("great job finishing homework")
test_value=0
safety_counter=0
while test_value==0:
    print("this loop never stops-it gos on for infinity")
    safety_counter+=1
    if safety_counter==3:
        print("stopping here on purpose a real infinity loop never stops")
        break
    print("\n\n===HOMEWORK COMPLETION SUMMARY===")
    print("work assigned : ",original_count)
    print("work completed: ",completed_count)
    print("remaining work: ",original_count-completed_count)
    print("==================================")