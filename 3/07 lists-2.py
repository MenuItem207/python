# you can put anything in a list
random_list = [
    1,
    "hello",
    True,
    # this is a list in a list!
    [
        "wow",
        "hiiii",
        "huhhhh",
    ],
]

# to access lists within lists, we can chain variable_name[][][][][]
print(random_list[3][2])

# for loops work very well with lists
for i in range(len(random_list)):
    print(random_list[i])
