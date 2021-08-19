class people():
    """Represents a person"""

    def __init__(self, age):
        """Initializes a person's attributes"""
        self.age = age

    def stage_of_life(self):
        """ Returns a string containing the person's stage of life""" 
        if self.age < 2:
            stage = "baby"
        elif  self.age < 4:
            stage = "toddler"
        elif self.age < 13:
            stage = "kid"
        elif self.age < 20:
            stage = "teenager"
        elif self.age < 65:
            stage = "adult"
        elif self.age >= 65:
            stage = "elder"
        return(stage)

# Create a list of people from 1 year to 100 years
people = [people(age) for age in list(range(1, 100, 8))]

# Get the stages of all the people in the list "people"
vowels = ["a", "e", "i", "o", "u"]
for person in people:
    stage = person.stage_of_life()
    if stage[0] in vowels:
        print(f"This person is an {stage}")
    else:
        print(f"This person is a {stage}")