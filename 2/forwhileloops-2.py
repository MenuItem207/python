# sometimes you wanna loop through something without knowing how many times its gonna take
lunch = input("what are you having for lunch")
lunch_is_egg = lunch == "egg"

while lunch_is_egg:
    print("again")
    lunch = input("what are you having for lunch")
    lunch_is_egg = lunch == "egg"
