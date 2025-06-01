#def say_something(word, word2, word3):
#    print(word)
#    print(word2)
#    print(word3)
#
#say_something('Hello', 'Mike', 'Nancy')

#def say_something(*args):
#    print(args)
#
#say_something('Hello', 'Mike', 'Nancy')


def say_something(*args):
    for arg in args :
        print(arg)

say_something('Hello', 'Mike', 'Nancy')

t = ('Mike', 'Nancy')
say_something('Hi!', *t)