# if statements work alone too!
lunch = input("What would you like to eat?: ")

if lunch == "apple":
    # only run if lunch is "apple"
    print("Thats good")

print("thats all")

# if theres multiple conditions use "elif":
dinner = input("What would you like to eat for dinner")
if dinner == "rice":
    print("I LOVE RICE")
elif dinner == "noodles":
    print("I LOVE noodles")
elif dinner == "eggs":
    print("I LOVE eggs")
else:
    print("you have bad taste")

# * Excercise
# Write a function that:
# 1. takes in an input, either "tall" or "short"
# 2. a) if "tall", take another input and ask for the user's height
# 3. a) if height > 175 print "you're tall!" else print "you're short!"
# 2. b) if "short", take another input and ask if the user is a guy or girl
# 3. b) if "guy", print "you're a short king" else print "you're a short queen"
