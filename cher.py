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
