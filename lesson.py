# import lesson_package.utils
# from lesson_package import utils
from practice.lesson_package.tools.utils import say_twice
from lesson_package.talk import human

# r = lesson_package.utils.say_twice('hello')

# r = utils.say_twice('hello')

r = say_twice('hello')

print(r)

print(human.sing())
print(human.cry())