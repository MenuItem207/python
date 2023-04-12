# sometimes you wanna loop through something without knowing how many times its gonna take
# Example of using a while loop to count down from 5 to 1
countdown = int(input("Enter any number: "))

# a while loop will run the code inside as long as the condition is TRUE
while countdown > 0:
    print(countdown)
    countdown -= 1

print("Blast off!")

# * Excercise
# Write a program that uses a while loop to repeatedly ask the user to enter a positive integer.
# If the user enters a negative number or zero, the program should print an error message and ask for a positive integer again.
# If the user enters a positive integer, the program should print a message indicating whether the number is even or odd.
