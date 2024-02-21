def greet(name):
    print("Hello, " + name + '!')
    greet_2(name)
    print("get ready to say bye")
    bye()
    return '5'

def greet_2(name):
    print("how are you, " +  name)

def bye():
    print('ok, bye')

print(greet('aidina'))

'''
Hello, aidina!
how are you, aidina
get ready to say bye
ok, bye
5 
- результат вывода функции greet

Таким образом, функция greet находится в незавершенном состоянии, так как его вложенные функции еще долны отработаться и при этом вывести 5

это и есть стек, выстраивается очередь запуска каких то операций в коде
'''

def fact(x):
    if x == 1:
        return 1
    else:
        print(f"текущий х - {x}")
        return x * fact(x -1)
    
print(fact(3))