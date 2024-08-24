list=[42,69,322,-9,13,0,99,-5,9,7,-6,5]
a=0                                      #счётчик
while a<len(list):                       #условие в цикле
    element=list[a]                      #новая переменная = list[a]
    if element<0:                        #если эелемент списка <0 = break
        break
    print(element)                       #вывод переменной element
    a=a+1                                #пербор значений






