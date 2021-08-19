# Store the  users of a website
current_users = ["ademar701", "miguel_pro123", "makanas_master2000", "marco_gamer",
            "violeta_vh79", "admin", "alex_chief", "ntonio2004"]
new_users = ["alex_chief", "ayrton2002", "yahir_boss400", "antonio2004", 
            "juan_maquina"]

# Check if the new usernames are available
current_users_lower = [user.lower() for user in current_users]
for user in new_users:
    if user.lower() in current_users_lower:
        print("The username is already taken")
    else:
        print("The username is available")

