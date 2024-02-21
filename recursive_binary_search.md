# Рукурсивный бинарный поиск
```py
def recursive_binary_search(nums, target):
    if len(nums) == 0:
        return False
    else:
        midpoint = (len(nums)) // 2
        if nums[midpoint] == target:
            return True
        else:
            if nums[midpoint] < target:
                return recursive_binary_search(nums[midpoint + 1:],target)
            else:
                return recursive_binary_search(nums[:midpoint],target)

num = [1,2,3,4,5,6,7,8,9,10]
print(recursive_binary_search(num, 11))
```

Когда работаем с руксирией необходимо обязат указать условия остановки функции
В нащем случае это 2 условия остановки:
1. Первая - когда мы говорим, что если список пуст, то нужно вернуть Фолс
2. Вторая - когда индекс мидпоинта == таргету, то пусть вернет Тру
В остальных случаях повторяй функцию

## Рекурсивная глубина 
- это сколько раз функция себя вызывала

* Итеративное решение - это когда в рукуирсивной функции были использованы какие то элементы цикла
