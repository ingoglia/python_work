invite = ['Mike', 'Joe', 'Josh', 'Harold', 'Cardin']
'''
print('Hey '+ invite[0] + "! Would you like to come to dinner?")
print('Hey '+ invite[4] + "! Would you like to come to dinner?")
print('Hey '+ invite[3] + "! Would you like to come to dinner?")
print(invite[1] + " and " + invite[2] + "! Come over for dinner!")
print('Hey ' + invite[0] +', '+ invite[1] +', '+  invite[2] + ', '+invite[3] +', '+ invite[4] +". I found a bigger table in the basement!")
invite.insert(0,'Dean')
invite.insert(3,'Jake')
invite.append('Lionel')
print(invite)
print('Hey ' + invite[0] +', '+ invite[1] +', '+  invite[2] + ', '+invite[3] +', '+ invite[4] +", "+ invite[5] +", " + invite[6] + ", " + invite[7] +". Would all of you like to come to my place for some tacos?")
print("Haha.... well... turns out I can only invite 2 people")
friend0 = invite.pop(0)
print("sorry " + friend0 + ", see you next time.")
friend1 = invite.pop(0)
print("sorry " + friend1 + ", see you next time.")
friend2 = invite.pop(0)
print("sorry " + friend2 + ", see you next time.")
friend3 = invite.pop(0)
print("sorry " + friend3 + ", see you next time.")
friend4 = invite.pop(0)
print("sorry " + friend4 + ", see you next time.")
friend5 = invite.pop(0)
print("sorry " + friend5 + ", see you next time.")
print("So, " + invite[0] + " and " + invite[1] + ", let me know if you guys still want to come.")
invite.remove('Cardin')
invite.remove('Lionel')
print(invite)
'''
print("I am inviting " + str(len(invite)) + " people to dinner.")
