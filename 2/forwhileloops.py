# lets say you wanna count to 10, you can either:
print("Counting: 1")
print("Counting: 2")
# ...
print("Counting: 10")

# OR you could use a FOR loop
# the following for loop creates the variable i = 0 and runs the code inside
# everytime the code completes, it loops over and i increases by 1
# this stops when i == 11
for i in range(11):  # we put the number you want to stop BEFORE
    print("Counting: " + str(i))

# * Excercise
# 1. figure out how to count to 100,
# 2. edit the previous code to start from 50
# 3. edit the previous code to only count in multiples of 5 using if elses
# 4. count in multiples of 5 without the if elses
