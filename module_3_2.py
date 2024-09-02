def send_mail(message, recipient, sender='n.sk@ya.ru'):

    if '@' not in recipient and '@' not in sender:
        print('Невозможно отправить письмо с', sender, 'на', recipient)

    # eсли нет в адресе получателя '.com',         и нет '.ru'                        и нет '.net'
    elif not recipient.endswith('.com') and not recipient.endswith('.ru') and not recipient.endswith('.net'):
        print('Невозможно отправить письмо с', sender, 'на',recipient)

    # то же с отправителем
    elif not sender.endswith('.com') and not sender.endswith('.ru') and not sender.endswith('.net'):
        print('Невозможно отправить письмо с', sender, 'на алрес', recipient)

    elif recipient == sender:
        print('Нельзя отправить письмо себе')

    elif sender == 'n.sk@ya.ru':       # отпр по умолчанию
        print('Письмо успешно отправлено с адреса', sender, 'на адрес',recipient)

    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с',sender,' на',recipient)

send_mail('Проверка связи', 'mail@osk.ru')    #Проверка сязи
send_mail('Нельзя отпрвить самомк себе', 'n.sk@ya.ru', 'n.sk@ya.ru')
send_mail('Письмо успешно отправлено', 'mail@osk.ru', 'n.sk@ya.ru')
send_mail('Неверный отправитель', 'mail@osk.ru', 'n.sk@ya.net')      # Разобраться
send_mail('Невозможно отправить - нет домена', 'mail@osk', 'n.sk@ya.com')
send_mail('Невозможно отправить - нет @', 'mail@osk.ru', 'n.skya.ru')


# Написать код с поздравлениями