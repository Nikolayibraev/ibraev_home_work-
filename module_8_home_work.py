#--------------- H O M E  W O R K  (M O D U L E _ 8 _ 1) ---------------

# def add_everything_up(a,b):
#
#     try:
#         # если это разные типы данных выполняем конкатенацию
#             if isinstance(a, float, int) and isinstance(b, float,int):
#                 return a+b
#             elif isinstance(a,str) and isinstance(b,str):
#                 return a+b
#
#     except TypeError:
#         return str(a) + str(b)
#
# print(add_everything_up(3, 3))
# print(add_everything_up('яблоко', 4215))
# print(add_everything_up(123.456, 7))


# -------------- В Т О Р О Й  В А Р И А Н Т ---------------

def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)


print(add_everything_up(3, 3))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.2, 1.1))
