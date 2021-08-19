# Store the ice cream flavors available
i_c_flavors = ["vanilla", "strawberry", "lemon", "chocolate"]
print("The ice cream flavors available are:")
for flavor in i_c_flavors:
    print(flavor)

# Use a variety of conditional tests
print("\nIs vanilla ice cream availabe?")
print("vanilla" in i_c_flavors)

print("Is blueberry ice cream avaliable?")
print("blueberry" in i_c_flavors)

print("Is coconut ice cream available?")
print("coconut" in i_c_flavors)

print("Are there more than 10 flavors available?")
print(len(i_c_flavors) > 10)

print("Are there more than 3 flavours available?")
print(len(i_c_flavors) > 3)

# Check for a specific flavor
ask_for_flavor = input("Do you want to know if an ice cream flavour is availabe?"
         "\nPress \"n\" if you don't ")
if ask_for_flavor != "n":
    desired_flavor = input("What is the ice cream flavor you want to check for? ")
    print(desired_flavor in i_c_flavors)
else:
    exit()        