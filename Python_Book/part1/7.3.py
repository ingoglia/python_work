number = input("Tell me a number and I'll tell you something interesting... ")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is divisible by 10... woah....")
else:
    print(str(number) + ' is not divisible by 10... boo...')
