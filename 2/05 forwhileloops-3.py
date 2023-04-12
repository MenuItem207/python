# "continue" is used to skip the current "round"
# "break" is used to stop the entire loop
# Example using break and continue in a for loop

# loop through numbers 0 to 9
for i in range(10):
    # if i is even, skip to the next iteration / round
    if i % 2 == 0:
        continue
    # if i is 7, exit the loop
    if i == 7:
        break
    # print the current value of i
    print(i)

print("Loop complete")

# stop when user enters "stop"
name = input("What's your name?: ")
while True:
    # stop only when the user enters "stop"
    if name == "stop":
        break

    name = input("What's your name?: ")

# * Excercise
# Write a program that uses a while loop to repeatedly ask the user to enter a positive integer.
# The program should keep a running total of the even numbers entered,
# but should stop asking for input when the user enters a number that is not divisible by 3.
# Use the 'break' and 'continue' keywords in your solution.
