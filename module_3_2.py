def send_email(message, recipient,*, sender='university.help@gmail.com'):
    at1 = recipient.count('@')
    at2 = recipient.endswith((".com", ".ru", ".net"), -4)
    dm1 = sender.count('@')
    dm2 = sender.endswith((".com", ".ru", ".net"), -4)
    #print(at1,  at2, dm1, dm2)
    if at1 == at2 == dm1 == dm2 == 1:
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        elif sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
send_email('Проверка связи', 'vasyok1337@gmail.com', sender='university.help@gmail.com')
send_email('Проверка связи', 'university.help@gmail.com', sender='123university.help@gmail.com')
send_email('Проверка связи', 'vasyok1337@gmail.net', sender='university.help@@@gmail.com')
send_email('Проверка связи', 'vasyok1337@gmail.net', sender='vasyok1337@gmail.net')

