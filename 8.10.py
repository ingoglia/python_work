def show_magicians(magicians):
    """Prints the name of each magician in the list"""
    for magician in magicians:
        print("The name of this magician is " + magician + ".")

def make_great(magicians):
    """Adds 'the great' to every magician."""
    while magicians:
        great_magician = "The Great " + magicians.pop()
        great_magicians.append(great_magician)
        
magicians = ['hudini', 'david copperfield', 'zooby']
great_magicians = []

make_great(magicians)
show_magicians(great_magicians)
