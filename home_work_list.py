#TASK_1.0 (SUM)
print('TASK_1')
my_list=[1,2,3,4,5]
my_list.pop(2)
print(len(my_list))

my_list.sort(reverse=True)      #sum

new_list=['abc','def']
print(my_list+new_list)



#TASK_1.2 (A NEW VARIABLE)
print('TASK_1.2')
my_list=[1,2,3,4,5]         
my_list.pop(2)                            
print(len(my_list))

my_list.sort(reverse=True)  

new_list=['abc','def']  
var=my_list+new_list            #a_new_var
my_list=var
print(my_list)



#TASK_1.3 (.EXTEND)
print('TASK_1.3')
my_list=[1,2,3,4,5]         
my_list.pop(2)                           
print(len(my_list))

my_list.sort(reverse=True)  

new_list=['abc','def']           #.extend
my_list.extend(new_list)
print(my_list)



#TASK_2
print('TASK_2')                          #concatenation_lists_by(__add__)
fist_list=[4,2,3,9]
second_list=[12,86,54,90]
print(fist_list.__add__(second_list))


