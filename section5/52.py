#位置引数のタプル化
def say_something(word, *args):
    print('word =', word)
    for arg in args:
        print(arg)
    
say_something('Hi!!!', 'Mike', 'Nance')

""" t = ('Mike', 'Nance')
say_something('Hi!!!', *t) """