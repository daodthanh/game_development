# bank1_one_account.py
account_name = 'Joe'
account_balance = 100
account_password = 'soup'

while True:
  print()
  print('Press b to get the balance')
  print('Press d to make a deposit')
  print('Press w to make a withdrawal')
  print('Press s to show the account')
  print('Press q to quit')
  print()

  action = input('What do you want to do? ')
  action = action.lower()
  action = action[0]
  print()

  if action == 'q':
    break
  if action == 's':
    print('Show: ')
    print('Name: ', account_name)
    print('Balance: ', account_balance)
    print('Password', account_password)
    print()
  if action == 'b':
    print('Get Balance: ')
    user_password = input('Please enter the password: ')
    if user_password != account_password:
      print('Incorrect password')
    else:
      print('Your balance is: ', account_balance)

  if action == 'd':
    print('Deposit: ')
    user_deposit_amount = int(input("Please enter amount to deposit: "))
    user_password = input('Please enter the password: ')

    if user_deposit_amount < 0:
      print('You cannot deposit a negative amount!')
    elif user_password != account_password:
      print('Incorrect password')
    else:
      account_balance += user_deposit_amount
      print('Your new balance: ', account_balance)

  if action == 'w':
    print('Withdraw: ')
    user_withdraw_amount = int(input("Please enter the ammount to withdraw: "))
    user_password        = input('Please enter the password: ')

    if user_withdraw_amount < 0:
      print('You cannot withdraw a negative amount')

    elif user_withdraw_amount > account_balance:
      print('You cannot withdraw more than you have in your account')
    else:
      if user_password != account_password:
        print('Incorrect password')
      else:
        account_balance -= account_balance - user_withdraw_amount
        print('Your new balance is: ', account_balance)

print('Done')




