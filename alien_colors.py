class Alien():
    """Represents an alien"""
    
    def __init__(self, color):
        self.color = color

    def get_points(alien):
        """Get an alien instance's points"""
        if alien.color == "green":
            print("You just earned 5 points")
        elif alien.color == "yellow":
            print("You just earned 10 points")
        elif alien.color == "red":
            print("You just earned 15 points")        

# Create three alien instances
green_alien = Alien("green")
yellow_allien = Alien("yellow")
red_alien = Alien("red")

green_alien.get_points()
yellow_allien.get_points()
red_alien.get_points()