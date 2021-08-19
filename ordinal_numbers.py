# Store a list of numbers from 1 to 9
numbers = [x for x in range(1, 10)]

# Print the ordinal numbers from 1st to 9th
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")   
    else:
        print(f"{str(number)}th")
