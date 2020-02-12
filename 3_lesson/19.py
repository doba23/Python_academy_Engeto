data = {'user1': 'password1', 'Mark': '1234', 'Danny': 'qwert'}

user = input ('please enter username:')
password = input ('please enter password:')

if data.get( user, 0) == password:
    print('Permission granted')
else :
    print('Password or username is wrong')
