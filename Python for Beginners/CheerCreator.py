# Cheer Creator

# Cheering for your favourite team.  If they got over 10 yards further down the field, give a high 
# five.  If they don't move forward, say shh, and if the move forward 10 yards or less, say Ra! for 
# every yard they moved in that play.

x = int(input())

if x > 10:
    print("High Five")
elif x < 1:
    print("shh")
else:
    print("Ra!" * x)
