from Bank import Bank
import re
import time
b = Bank('users.db')
while True:
    login = input('Login: ')
    try:
        pin = int(input('Pin: '))
    except ValueError:
        print('ValueError')
        continue
    if not b.auth(login, pin):
        print('Error login!')
        continue
    print('Успешная авторизация в системе')
    money = input('Сумма=')
    if not re.match(r'[0-9]+$', money):
        print('Error money')
        continue
    if not b.selectbalance():
        print('Error balance')
        continue

    if b.selectbalance() > int(money) and b.selectlimit() > int(money):
        if b.selectbalanceuser(login, pin) > int(money):
            b.updatebalance(b.selectbalance() - int(money))
            b.updatebalanceuser(login, pin, b.selectbalanceuser(login, pin) - int(money))
            print('Возьмите ваши деньги')
            print(f'На вашем счете осталось {b.selectbalanceuser(login, pin)}')
            print('Подождите...')
            time.sleep(7)
        else:
            print('У вас недостаточная сумма на балансе')
    else:
        print('Сумма в банкомате меньше указаной вами или лимит больше')

