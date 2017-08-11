filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

dummy = ''
for line in lines:
    dummy += line.strip()

print(dummy)
print(dummy)
print(dummy)
