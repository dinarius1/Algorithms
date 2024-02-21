import math
def func(a, b,c):
    D = (b ** 2) - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        return x1, x2
    elif D == 0:
        x = -b/2*a
        return x
    elif D < 0:
        return 'нет корней'

a,b,c = map(float, input().split(','))
result = func(a,b,c)
print(result)