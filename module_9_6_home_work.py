#--------------- H O M E  W O R K  (M O D U L E _ 9 _ 6) ---------------

def all_variants(text):
    length = len(text)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield text[start:end]


a = all_variants("abc")
for i in a:
    print(i)

