# --------------- ДОМАШНЯЯ РАБОТА ---------------

def multiplied_digits(number):
    str_num=str(number)
    first=int(str_num[0])    # отделяем первый символ str_num

    if len(str_num)>1:       # программа вызывает саму себя
        return first * multiplied_digits(int(str_num[1:]))

    else:                    # если <=1 return first
        return first         # завершение программы


result=multiplied_digits(10234)
print(result)