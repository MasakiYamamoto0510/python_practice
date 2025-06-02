l = ['Mon', 'tue', 'Wed', 'thu', 'Fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words :
        print(func(word))

# def sample_func(word):
#     return word.capitalize()

sample_func = lambda word: word.capitalize()

change_words(l, sample_func)