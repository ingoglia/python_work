from random import randint

class Die():
    """Model a die"""

    def __init__(self, sides):
        """Initialize the attributes"""
        self.sides = sides

    def roll_die(self):
        """Roll a die"""
        x = randint(1,self.sides)
        print(x)

six_sided = Die(6)
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()
six_sided.roll_die()

ten_sided = Die(10)
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()
ten_sided.roll_die()

twenty_sided = Die(20)
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()
twenty_sided.roll_die()

