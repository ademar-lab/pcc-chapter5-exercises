# Store a list of usernames a website has
usernames = ["ademar701", "miguel_pro123", "makanas_master2000", "marco_gamer",
            "violeta_vh79", "admin"]

def log_in(user):
    """Prints a personilized greeting when a user logs in"""
    if user == "admin":
        print("Hello admin!\nWould you like to see a status report?")
    else:
        print(f"Hello {user}! Welcome back")

# Print a greeeting to each user
for user in usernames:
    log_in(user)

# Check if there are any users
usernames = [] 
if usernames:
    print("We have usernames")
else:
    print("We need to find some usernames!")

