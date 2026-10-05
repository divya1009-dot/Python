team1=160
team2=90
team3=130
team4=70
team5=50
total=team1+team2+team3+team4+team5
average_per_team=total/5
print("total points",total)
print("average per team",average_per_team)
stars_per_point=3
reward_stars=total*stars_per_point
print("total reward stars",reward_stars)
boxes=total//25
leftover=total%25
print("full boxes pcked",boxes)
print("leftovers",leftover)
last_week=520
print("better than last week",total>last_week)
print("as good as last week",total==last_week)
print("worse than last week",total<last_week)
total+=30
print("total after bonus tasks",total)
total-=10
print("total after missing tasks",total)
boxes=total//25
print("final boxes packed",boxes)