title_name_1 = 'Мастер кода'
title_name_2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'




# И С П О Л Ь З О В А Н И Е  '%'
print('В команде %s' % (title_name_1), '%s' % (team1_num),'участников')
print('Итого сегодня в командах %s' % (team1_num), 'и', (team2_num),'участников')



# И С П О Л Ь З О В А Н И Е   М Е Т О Д A  '.F O R M A T'
print('Команда {title} решила {score} задачи'.format(title = title_name_2, score = score2))
print('Команда {title} решила задачи за {team1_time} c'.format(title = title_name_2, team1_time = team1_time))


# И С П О Л Ь З О В А Н И Е   F - С Т Р О К И
print(f'Команды решили {score1} и {score2} задач')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    print(f'Победа команды {title_name_1}!')
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    print(f'Победа команды {title_name_2}!')
else:
    print(f'Ничья')











