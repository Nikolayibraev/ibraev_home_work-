from false_math import divide as f_math
from true_math import divide as t_math

result1=f_math(40,4)
print(result1)                            #false_math
result2=f_math(11, 0)
print(result2)

result3=t_math(21,3)
print(result3)                             #true_math (inf)
result4=t_math(17, 0)
print(result4)

