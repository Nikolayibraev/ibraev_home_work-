# --------------- MODULE_3_HARD ---------------

def calculate_structure_sum(data):
    res=0
    for i in data:
        if isinstance(i, list) or isinstance (i, tuple) or isinstance(i, set):
            res+=calculate_structure_sum(i)
        elif isinstance(i, dict):
            res+=calculate_structure_sum(i.items())    # all keys and values of dictionary
        elif isinstance(i, int):                       # all digit values
            res+=i
        elif isinstance(i, str):
            res += len(i)
    return res


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5}, #dict
    (6, {'cube': 7, 'drum': 8}),                # use *args
    "Hello",
    ((), [{(2,'Urban', ('Urban2',35))}])      # use *args /// tuple in tuple in set in list
]

result = calculate_structure_sum(data_structure)
print(result)

#[]=list
#()=tuple
#{}=set
#{'key':value}=dict