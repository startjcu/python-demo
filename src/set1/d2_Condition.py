account = 'star'
password = '123456'

print('please input account: ')
user_account = input()
print('please input password: ')
user_password = input()

if user_account == account and user_password == password:
    print('success')
else:
    print('fail')
