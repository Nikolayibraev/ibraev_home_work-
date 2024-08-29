import random
list = [1,2,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def island():
    log = random.choice(list[2:])
    return log
log = island()
print(f'Значение: {log}')

for i in range(1,20):
    for j in range(i+1,len(list)):      # J всегда значние больше чем I
        if log%(i+j)==0:

            print(i,j, end=' ')