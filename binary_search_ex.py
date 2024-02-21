# Первый способ - лмнейный
def func(s):
    res = []

    for i in s.lower():
        if i.isalpha():
            res.append(i)
        
    res = ''.join(res)
    
    if res == res[::-1]:
        return True
    return False


# print(func("A man, a plan, a canal: Panama"))

# Второй способ - бинарный

def func(s : str):
    s = s.lower()
    res = ''.join(filter(str.isalnum, s))
    return res == res[::-1]

# print(func("A man, a plan, a canal: Panama"))

def serch_summ_num(n):
    