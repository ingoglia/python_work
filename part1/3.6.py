invite = ['Mike', 'Joe', 'Josh', 'Harold', 'Cardin']
print('Hey '+ invite[0] + "! Would you like to come to dinner?")
print('Hey '+ invite[4] + "! Would you like to come to dinner?")
print('Hey '+ invite[3] + "! Would you like to come to dinner?")
print(invite[1] + " and " + invite[2] + "! Come over for dinner!")
print('Hey ' + invite[0] +', '+ invite[1] +', '+  invite[2] + ', '+invite[3] +', '+ invite[4] +". I found a bigger table in the basement!")
invite.insert(0,'Dean')
invite.insert(3,'Jake')
invite.append('Lionel')

print('Hey ' + invite[0] +', '+ invite[1] +', '+  invite[2] + ', '+invite[3] +', '+ invite[4] +", "+ invite[5] +", " + invite[6] + ", " + invite[7] +". Would all of you like to come to my place for some tacos?")
