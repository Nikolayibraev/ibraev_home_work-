def get_matrix(m,n,value):
    matrix=[]
    for i in range(n):                # ищем кол-во внутренних списов  N и кладём в I
        matrix.append([])             # и добавляем пустой список в первый список
        for j in range(m):            #ищем значения для M и кладём в J
            matrix[i].append(value)   # вставляем значения в строки в певом цикле
    return matrix                            #возвращаем функцию

result1=get_matrix(2,5,7)
result2=get_matrix(4,6,3)       #создаем переменные равные значениям функции
result3=get_matrix(4,8,2)

print(result1)
print(result2)                              #вывод результата
print(result3)

