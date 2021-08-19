# Store my favorite fruits
favorite_fruits = ["lichi", "dragon fruit", "kiwi", "cherries", "watermelon"]

def inside_fav_fruits(fruit):
    """Checks if a kind of fruit is inside the list "favorite fruits" """
    if fruit in favorite_fruits:
        print(f"You love {fruit}!")
    elif fruit[-1] == "s":
        print(f"{fruit.title()} are not your favorite fruit")
    else:
        print(f"{fruit.title()} is not your favorite fruit")

# Store a list of fruits to check if they are in "favorite_fruits"
fruits_to_check = ["mango", "cherries", "watermelon", "coconut"]

for fruit in fruits_to_check:
    inside_fav_fruits(fruit)