def sum(x):
    if len(x) == 0:
        return 0
    
    while len(x) > 0:
        print(x)
        return x[0] + sum(x[1:])

# print(sum([4,2,10,10]))

def total(x):
    if x == []:
        return 0
    return 1 + total(x[:-1])

print(total([1,2,3]))



def maxi(x):
    if len(x) == 2:
        return x[0] if x[0] > x[1] else x[1]
    maximum = max(x[1:])
    return x[0] if x[0] > maximum else maximum

