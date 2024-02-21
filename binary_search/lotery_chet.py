def func(a,b,c):
    if (a % 2 == 0 and b % 2 == 0 and c % 2 == 0) or (a % 2 != 0 and  b % 2 != 0 and c % 2 != 0):
        return 'win'
    return 'lose'

a,b,c = map(float, input().split(','))
result = func(a,b,c)
print(result)