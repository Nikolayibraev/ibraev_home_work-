#--------------- H O M E  W O R K  (M O D U L E _ 9 _ 3) ---------------

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))