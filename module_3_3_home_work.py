def print_parameters(a=1,b='address',c=True):
    print(a,b,c)

#-------------_ ПАРАМЕТРЫ ПО УМОЛЧАНИЮ --------------
print_parameters()
print_parameters (b=25, c=[1,2,3])

#-------------- РАСПАКОВКА ПАРАМЕТРОВ --------------
values_list=[1,'host',['list','main']]
values_dict={'a':1,'b':'address','c':True}

print_parameters (*values_list)
print_parameters (**values_dict)

#--------- РАСПАКОВКА + ОТДЕЛЬНЫЕ ПАРАМЕТРЫ ---------
values_list_2=[43,'yoshkar-ola']

print_parameters(*values_list_2,12)