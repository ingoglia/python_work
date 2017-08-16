file1 = 'cats.txt'
file2 = 'dogs.txt'

def print_file(filename):
    """opens files and prints them"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
            print(contents)
    except FileNotFoundError:
        msg = "No file " + filename + " found."
        print(msg)
        
print_file(file1)
print_file(file2)
print_file('cow.txt')
