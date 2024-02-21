from collections import deque

graph = {} # Графы лучше иллюстрирвоать через хеш-таблицы.

graph['you'] = ['bob', 'alice', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['tom', 'jonny']
graph['alice'] = ['peggy'] # Даже если два узла показывает на одного человека (узла), то мы его тоже записываем. Записывем в качестве значений только те узлы, от которых узел-ключ имеет направления.
graph['peggy'] = [] # Они имеют пустые знаечния, так как являются ненаправленными узлами
graph['tom'] = []
graph['jonny'] = []
graph['anuj'] = []
# print(graph)

def search(name):
    search_queue = deque() # Создаем очередь
    search_queue += graph[name] # добавляем все значения ключа "you", это значит, что добавяться ['bob', 'alice', 'claire']

    print(search_queue) # deque(['bob', 'alice', 'claire'])
    searched = []

    while search_queue:
        '''
        Пока не будет пуст список с очередью - цикл не закончиться
        '''
        person = search_queue.popleft() # Берем первый элемент из очереди - 'bob'

        print(person)
        if not person in searched: # Проверяем был ли он уже проверен или нет
            if person_is_seller(person): # Проверяем его на условие, является ли он продавцом
                print('The seller is ' + person + '!')
                return True
            else:
                search_queue += graph[person] # Если же нет, то добавляем все значения ключа боба - ['anuj', 'peggy'] в очередь в конец
                print(search_queue)
                searched.append(person)
    return False
    

def person_is_seller(person):
    print(person + '1')
    return person[0] == 'c'

print(search('you'))