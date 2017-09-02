string1 = 'ferret'
string2 = 'mouse'
print('does ferret = mouse?')
print(string1 == string2)

string3 = 'Mouse'
print('is a Mouse a mouse?')
print(string2 == string3)
print('are you sure? Try again')
print(string2 == string3.lower())

print('does 3 = 2?')
print(3 == 2)

print('is 3 > 2?')
print(3 > 2)

print('is 3 >= 2?')
print(3 >= 2)

print("I don't think that 8 = 4")
print(8 != 4)

print('is 6 <= 8?')
print(6 <= 8)

print('is 5 < 3?')
print(5 < 3)

religion1 = 'christian'


belief1 = 'god'


religion = 'religion'
belief = 'belief'

print( 'is it the case that a christian is both a deity and a believer?')
print( 'christian' == 'christian' and 'christian' == 'god' )
print( 'is it the case that a christian is either a deity or a believer?')
print( 'christian' == 'christian' or 'christian' == 'god' )

fruits = ['banana', 'blueberry', 'raspberry', 'melon']
print('is there a banana?')
print('banana' in fruits)
print('is there a raspberry?')
print('raspberry' in fruits)
print('there are no strawberries are there.')
print('strawberries' not in fruits)
