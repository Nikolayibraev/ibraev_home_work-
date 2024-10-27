#--------------- H O M E  W O R K  (M O D U L E _ 7 _ 5) ---------------
import os
import time

directory = '.'
for root, dirs, files in os.walk(directory):
    for i in files:
        filepath = os.path.join(root, i)         # полный путь к файлу
        filetime = os.path.getmtime(filepath)    # последнее изменение файла
        formatted_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(filetime))
        filesize = os.path.getsize(filepath)     # Получение размера файла
        parent_dir = os.path.dirname(filepath)   # Получение род директории
        print(f'Обнаружен файл: {i}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')