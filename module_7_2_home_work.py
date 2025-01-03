def custom_write(file_name, strings):
    strings_positions = {}

    file = open(file_name, 'w', encoding='utf-8')

    index = 1
    for i in strings:
        byte_position = file.tell()
        file.write(i + '\n')
        strings_positions[(index, byte_position)] = i
        index += 1
    file.close()
    return strings_positions




info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for j in result.items():
    print(j)