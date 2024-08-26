list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# a=0                                            #счётчик

prime = []
not_prime = []
is_prime = True  # сравниваем

for i in list:  # цикл перебирает наш список и кладет в i
    if i > 1:  # все числа > 1
        for j in range(2, i):  # цикл перебирает делители от 2 и примеряет их i
            if i % j == 0:  # элементы списка делим на делители == 0
                is_prime = False  # Проверячем, если есть остаток - False
                break  # завершаем цикл
        if is_prime:  # если проверка = False
            prime.append(i)  # добавляем i в prime

        else:
            not_prime.append(i)  # и наоборот
        is_prime = True

print(prime)
print(not_prime)
